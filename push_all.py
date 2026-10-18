#!/usr/bin/env python3
"""
push_all.py - 使用AI自动生成commit信息并推送到远程仓库
"""

import os
import subprocess
import sys
from datetime import datetime

import requests

DEFAULT_AI_URL = os.environ.get(
    "AI_URL", "http://127.0.0.1:1234/v1/chat/completions"
)


class GitAIAutoCommit:
    def __init__(self, ai_url=DEFAULT_AI_URL):
        self.ai_url = ai_url
        self.remotes = ["origin"]  # 要推送的远程仓库

    def run_command(self, args, capture_output=True):
        """运行命令（参数数组方式，避免 shell 注入）"""
        try:
            if capture_output:
                result = subprocess.run(
                    args, capture_output=True, text=True
                )
                return result.stdout.strip(), result.stderr.strip(), result.returncode
            else:
                result = subprocess.run(args)
                return "", "", result.returncode
        except Exception as e:
            return "", str(e), 1

    def get_git_status(self):
        """获取Git状态信息"""
        status, _, _ = self.run_command(["git", "status", "--porcelain"])
        staged_files, _, _ = self.run_command(
            ["git", "diff", "--cached", "--name-only"]
        )
        branch, _, _ = self.run_command(["git", "branch", "--show-current"])

        return {
            "status": status,
            "staged_files": staged_files,
            "branch": branch,
        }

    def generate_commit_message_ai(self, git_info):
        """使用AI生成commit信息"""
        prompt = f"""我正在 hugo 程序中进行编辑，基于以下Git变更信息，生成一个简洁、专业的commit信息。

当前分支: {git_info['branch']}

变更状态:
{git_info['status']}

已暂存文件:
{git_info['staged_files']}

请生成符合约定式提交(Conventional Commits)的commit信息，格式：类型(范围): 描述
例如：feat[auth]: 添加用户登录功能

只返回commit信息，不要有其他内容。"""

        try:
            response = requests.post(
                self.ai_url,
                json={
                    "model": "local-model",
                    "messages": [
                        {
                            "role": "system",
                            "content": "你是Git助手，专门生成commit信息。",
                        },
                        {"role": "user", "content": prompt},
                    ],
                    "max_tokens": 100,
                    "temperature": 0.7,
                },
                timeout=10,
            )

            if response.status_code == 200:
                content = response.json()["choices"][0]["message"]["content"]
                return content.strip()
        except Exception as e:
            print(f"AI生成失败: {e}")

        # 备用方案
        return f"chore: 自动提交 {datetime.now().strftime('%Y-%m-%d %H:%M')}"

    @staticmethod
    def sanitize_commit_message(msg):
        """清理 commit 信息（去除换行，防止多行 -m 参数问题）"""
        return " ".join(msg.split())[:200]

    def auto_add_files(self):
        """自动添加变更文件"""
        print("📁 检测变更文件...")

        status, _, _ = self.run_command(["git", "status", "--porcelain"])
        if not status:
            print("❌ 没有检测到变更")
            return False

        print("检测到以下变更:")
        self.run_command(["git", "status", "--short"], capture_output=False)

        # 自动添加所有变更文件（.gitignore 已排除构建产物和敏感文件）
        print("\n➕ 添加所有变更文件...")
        _, _, code = self.run_command(["git", "add", "-A"])
        return code == 0

    def commit_changes(self, commit_msg):
        """执行提交"""
        print(f"\n💾 提交更改: {commit_msg}")
        _, _, code = self.run_command(["git", "commit", "-m", commit_msg])
        return code == 0

    def push_to_remotes(self):
        """推送到所有远程仓库"""
        print("\n🚀 推送代码到远程仓库...")

        branch, _, _ = self.run_command(["git", "branch", "--show-current"])
        if not branch:
            branch = "main"

        success_count = 0
        for remote in self.remotes:
            print(f"\n推送至 {remote} ({branch})...")
            _, stderr, code = self.run_command(
                ["git", "push", remote, branch]
            )

            if code == 0:
                print(f"✅ {remote} 推送成功")
                success_count += 1
            else:
                print(f"❌ {remote} 推送失败")
                if stderr:
                    print(f"   错误: {stderr[:100]}")

        return success_count

    def main(self):
        """主流程"""
        print("=" * 50)
        print("🤖 Git AI 自动提交推送工具")
        print("=" * 50)

        # 检查是否在Git仓库
        _, _, code = self.run_command(["git", "rev-parse", "--git-dir"])
        if code != 0:
            print("❌ 当前目录不是Git仓库")
            return 1

        # 1. 自动添加文件
        if not self.auto_add_files():
            return 1

        # 2. 生成commit信息
        print("\n🧠 生成commit信息...")
        git_info = self.get_git_status()
        commit_msg = self.sanitize_commit_message(
            self.generate_commit_message_ai(git_info)
        )

        print(f"📝 AI生成的commit信息: {commit_msg}")

        # 3. 确认commit信息
        confirm = input(
            "\n使用这个commit信息？(Y:使用/E:编辑/N:取消): "
        ).strip().upper()

        if confirm == "E":
            new_msg = input("请输入新的commit信息: ").strip()
            if new_msg:
                commit_msg = self.sanitize_commit_message(new_msg)
            else:
                print("使用原信息")
        elif confirm == "N":
            print("取消提交")
            return 0

        # 4. 提交
        if not self.commit_changes(commit_msg):
            print("❌ 提交失败")
            return 1

        # 5. 推送
        success_count = self.push_to_remotes()

        print("\n" + "=" * 50)
        print(
            f"🎉 完成！成功推送到 {success_count}/{len(self.remotes)} 个远程仓库"
        )

        # 显示最终状态
        print("\n📊 最终状态:")
        self.run_command(["git", "log", "--oneline", "-2"], capture_output=False)

        return 0


if __name__ == "__main__":
    script = GitAIAutoCommit()
    sys.exit(script.main())
