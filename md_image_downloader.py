import os
import re
import requests
import argparse
from urllib.parse import urlparse
from pathlib import Path
from typing import List, Tuple, Optional, Dict
import time
import hashlib
import json

class HugoImageProcessor:
    def __init__(self, config_file: str = None, **kwargs):
        """
        Hugo优化的Markdown图片处理器
        
        Args:
            config_file: 配置文件路径
            **kwargs: 配置参数
        """
        # 默认配置
        self.config = {
            # 输入输出
            'md_file': None,
            
            # 路径配置 - 关键修改
            'storage_dir': 'static/assets/post_images',  # 实际存储目录
            'md_path_prefix': '/assets/post_images',     # Markdown中使用的路径前缀
            
            # 文件命名
            'naming_method': 'original',  # 'original', 'hash', 'timestamp', 'sequential'
            'use_post_slug': True,
            'post_slug': '',
            
            # 下载设置
            'overwrite_existing': False,
            'download_timeout': 30,
            'delay_between_requests': 0.3,
            
            # 请求头
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'referer': 'https://blog.csdn.net/',
            'extra_headers': {},
            
            # 处理选项
            'backup_original': True,
            'log_file': 'image_processor.log',
            
            # 其他
            'verbose': False,
        }
        
        # 从配置文件加载（如果存在）
        if config_file and os.path.exists(config_file):
            self.load_config(config_file)
        
        # 从kwargs更新配置
        self.config.update({k: v for k, v in kwargs.items() if v is not None})
        
        # 正则表达式
        self.image_pattern = re.compile(r'!\[(.*?)\]\((https?://[^)\s]+)\)')
        
        # 统计信息
        self.stats = {
            'total_images': 0,
            'downloaded': 0,
            'failed': 0,
            'skipped': 0,
            'duplicates': 0
        }
        
        # URL到文件名的映射缓存
        self.url_to_filename = {}
        
        if self.config['verbose']:
            print("Hugo图片处理器初始化完成")
            print(f"配置: {json.dumps(self.config, indent=2, ensure_ascii=False)}")
    
    def load_config(self, config_file: str):
        """从JSON文件加载配置"""
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                loaded_config = json.load(f)
                self.config.update(loaded_config)
                if self.config['verbose']:
                    print(f"从 {config_file} 加载配置")
        except Exception as e:
            print(f"加载配置文件失败: {e}")
    
    def extract_image_links(self, content: str) -> List[Tuple[str, str, str, int, int]]:
        """
        从Markdown文件中提取所有图片链接
        
        Returns:
            List of tuples: (full_match, alt_text, image_url, start_pos, end_pos)
        """
        images = []
        for match in self.image_pattern.finditer(content):
            full_match = match.group(0)
            alt_text = match.group(1)
            image_url = match.group(2)
            start_pos = match.start()
            end_pos = match.end()
            images.append((full_match, alt_text, image_url, start_pos, end_pos))
        
        self.stats['total_images'] = len(images)
        return images
    
    def generate_filename(self, url: str, index: int = 0) -> str:
        """
        根据配置生成文件名
        
        Args:
            url: 图片URL
            index: 图片序号
            
        Returns:
            生成的文件名
        """
        parsed_url = urlparse(url)
        original_name = Path(parsed_url.path).name
        
        # 获取基本名称和扩展名
        if original_name:
            base_name, ext = os.path.splitext(original_name)
            if not ext:
                ext = self.guess_extension(url)
        else:
            base_name = ''
            ext = self.guess_extension(url)
        
        # 清理基础名称
        if base_name:
            # 移除可能的时间戳等
            base_name = re.sub(r'\d{4}[-_]\d{2}[-_]\d{2}[-_]\d{6}', '', base_name)
            base_name = re.sub(r'[^\w\-]', '_', base_name)
            base_name = base_name.strip('_')
        
        naming_method = self.config['naming_method']
        
        if naming_method == 'original' and base_name:
            # 使用原始文件名（清理后）
            filename = f"{base_name}{ext}"
        elif naming_method == 'hash':
            # 使用URL哈希
            url_hash = hashlib.md5(url.encode()).hexdigest()[:12]
            filename = f"{url_hash}{ext}"
        elif naming_method == 'timestamp':
            # 使用时间戳
            timestamp = int(time.time() * 1000)
            if base_name:
                filename = f"{timestamp}_{base_name}{ext}"
            else:
                filename = f"{timestamp}{ext}"
        elif naming_method == 'sequential':
            # 使用序号
            if self.config['use_post_slug'] and self.config['post_slug']:
                filename = f"{self.config['post_slug']}_{index+1:03d}{ext}"
            else:
                filename = f"image_{index+1:03d}{ext}"
        else:
            # 默认：组合方式
            if base_name:
                filename = f"{base_name}{ext}"
            else:
                url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
                filename = f"{url_hash}{ext}"
        
        # 添加文章slug前缀
        if self.config['use_post_slug'] and self.config['post_slug']:
            if not filename.startswith(f"{self.config['post_slug']}_"):
                filename = f"{self.config['post_slug']}_{filename}"
        
        # 确保文件名有效
        filename = re.sub(r'[^\w\-\.]', '_', filename)
        filename = filename.lower()  # 通常使用小写文件名
        
        return filename
    
    def guess_extension(self, url: str) -> str:
        """根据URL猜测文件扩展名"""
        parsed_url = urlparse(url)
        path = parsed_url.path.lower()
        
        # 常见图片扩展名
        extensions = {
            '.jpg': ['.jpg', '.jpeg', '.jpe'],
            '.png': ['.png'],
            '.gif': ['.gif'],
            '.webp': ['.webp'],
            '.svg': ['.svg'],
            '.bmp': ['.bmp', '.dib'],
            '.tiff': ['.tiff', '.tif']
        }
        
        for ext, patterns in extensions.items():
            for pattern in patterns:
                if path.endswith(pattern):
                    return ext
        
        # 尝试从Content-Type判断
        try:
            response = requests.head(url, timeout=5, headers={'User-Agent': self.config['user_agent']})
            content_type = response.headers.get('Content-Type', '').lower()
            if 'jpeg' in content_type or 'jpg' in content_type:
                return '.jpg'
            elif 'png' in content_type:
                return '.png'
            elif 'gif' in content_type:
                return '.gif'
            elif 'webp' in content_type:
                return '.webp'
        except:
            pass
        
        # 默认
        return '.jpg'
    
    def download_image(self, url: str, filename: str) -> bool:
        """
        下载图片到本地
        
        Args:
            url: 图片URL
            filename: 保存的文件名
            
        Returns:
            是否成功
        """
        # 构建完整保存路径
        storage_dir = Path(self.config['storage_dir'])
        filepath = storage_dir / filename
        
        # 检查是否已存在
        if filepath.exists() and not self.config['overwrite_existing']:
            if self.config['verbose']:
                print(f"  文件已存在: {filename}")
            return True
        
        try:
            # 添加延迟
            time.sleep(self.config['delay_between_requests'])
            
            # 构建请求头
            headers = {
                'User-Agent': self.config['user_agent'],
                'Referer': self.config['referer'],
                'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            }
            headers.update(self.config['extra_headers'])
            
            # 发送请求
            if self.config['verbose']:
                print(f"  正在下载: {url}")
            
            response = requests.get(
                url, 
                headers=headers, 
                stream=True, 
                timeout=self.config['download_timeout']
            )
            response.raise_for_status()
            
            # 验证内容类型
            content_type = response.headers.get('Content-Type', '')
            if not content_type.startswith('image/'):
                print(f"  警告: 不是图片类型: {content_type}")
                return False
            
            # 确保目录存在
            filepath.parent.mkdir(parents=True, exist_ok=True)
            
            # 保存文件
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            # 验证文件
            file_size = filepath.stat().st_size
            if file_size < 100:
                filepath.unlink()
                print(f"  警告: 文件太小，可能无效 ({file_size}字节)")
                return False
            
            if self.config['verbose']:
                print(f"  已下载: {filename} ({file_size:,} 字节)")
            return True
            
        except requests.exceptions.Timeout:
            print(f"  下载超时: {url}")
            return False
        except requests.exceptions.RequestException as e:
            print(f"  下载失败: {e}")
            return False
        except Exception as e:
            print(f"  保存失败: {e}")
            return False
    
    def process_markdown(self, md_file: str = None):
        """
        处理Markdown文件
        """
        if md_file:
            self.config['md_file'] = md_file
        
        if not self.config['md_file']:
            print("错误: 未指定Markdown文件")
            return
        
        input_file_path = Path(self.config['md_file'])
        if not input_file_path.exists():
            print(f"错误: 文件不存在: {input_file_path}")
            return
        
        print(f"\n{'='*60}")
        print(f"处理文件: {input_file_path}")
        print(f"图片存储: {self.config['storage_dir']}")
        print(f"引用路径: {self.config['md_path_prefix']}")
        print(f"{'='*60}")
        
        # 读取文件内容
        with open(input_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取图片
        images = self.extract_image_links(content)
        
        if not images:
            print("未找到网络图片链接")
            return
        
        print(f"找到 {len(images)} 个网络图片链接")
        
        # 备份原始文件
        if self.config['backup_original']:
            backup_path = input_file_path.with_name(f"{input_file_path.stem}_backup{input_file_path.suffix}")
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(content)
            if self.config['verbose']:
                print(f"已创建备份: {backup_path}")
        
        # 处理每张图片
        content_list = list(content)
        replacements = []
        
        for i, (full_match, alt_text, url, start_pos, end_pos) in enumerate(images):
            print(f"\n[{i+1}/{len(images)}] 处理: {alt_text[:50]}...")
            if self.config['verbose']:
                print(f"  原始URL: {url[:80]}...")
            
            # 生成文件名
            filename = self.generate_filename(url, i)
            
            # 避免重复下载相同URL
            if url in self.url_to_filename:
                if self.config['verbose']:
                    print(f"  重复URL，使用缓存: {self.url_to_filename[url]}")
                filename = self.url_to_filename[url]
                self.stats['duplicates'] += 1
            else:
                self.url_to_filename[url] = filename
            
            # 构建Markdown中使用的路径
            md_image_path = f"{self.config['md_path_prefix']}/{filename}"
            
            # 下载图片
            if not (Path(self.config['storage_dir']) / filename).exists() or self.config['overwrite_existing']:
                if self.download_image(url, filename):
                    self.stats['downloaded'] += 1
                else:
                    print(f"  ! 下载失败，保留原始链接")
                    self.stats['failed'] += 1
                    continue
            else:
                if self.config['verbose']:
                    print(f"  文件已存在: {filename}")
                self.stats['skipped'] += 1
            
            # 构建新的Markdown语法
            new_markdown = f"![{alt_text}]({md_image_path})"
            replacements.append((start_pos, end_pos, new_markdown))
            
            if self.config['verbose']:
                print(f"  新路径: {md_image_path}")
        
        # 执行替换（从后往前）
        replacements.sort(key=lambda x: x[0], reverse=True)
        for start_pos, end_pos, new_markdown in replacements:
            content_list[start_pos:end_pos] = new_markdown
        
        # 写入新文件（覆盖原文件）
        new_content = ''.join(content_list)
        
        with open(input_file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        # 输出统计信息
        print(f"\n{'='*60}")
        print("处理完成!")
        print(f"总图片数: {self.stats['total_images']}")
        print(f"成功下载: {self.stats['downloaded']}")
        print(f"跳过(已存在): {self.stats['skipped']}")
        print(f"重复URL: {self.stats['duplicates']}")
        print(f"失败: {self.stats['failed']}")
        print(f"输出文件: {input_file_path}")
        
        # 显示路径映射关系
        print(f"\n路径映射关系:")
        print(f"  实际存储: {self.config['storage_dir']}/")
        print(f"  Markdown引用: {self.config['md_path_prefix']}/")
        
        # 显示一些示例
        if self.url_to_filename:
            print(f"\n示例文件:")
            for url, filename in list(self.url_to_filename.items())[:3]:
                print(f"  {filename} -> {self.config['md_path_prefix']}/{filename}")

def main():
    parser = argparse.ArgumentParser(
        description='Markdown图片下载工具 - 专为Hugo优化',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
使用示例:
  基本使用:
    python md_image_downloader.py article.md
  
  指定保存目录和引用路径:
    python md_image_downloader.py article.md -s "static/assets/post_images" -p "/assets/post_images"
  
  使用文章slug作为文件名前缀:
    python md_image_downloader.py article.md --post-slug "my-article"
  
  使用配置文件:
    python md_image_downloader.py -c config.json article.md

路径说明:
  - 图片实际保存在: static/assets/post_images/
  - Markdown中引用: /assets/post_images/
  - Hugo会自动从static目录提供这些文件
        '''
    )
    
    # 主要参数
    parser.add_argument('md_file', nargs='?', help='Markdown文件路径')
    
    # 路径配置
    parser.add_argument('-s', '--storage-dir', 
                       default='static/assets/post_images',
                       help='图片实际存储目录 (默认: static/assets/post_images)')
    
    parser.add_argument('-p', '--path-prefix', 
                       default='/assets/post_images',
                       help='Markdown中使用的路径前缀 (默认: /assets/post_images)')
    
    # 文件命名
    parser.add_argument('-n', '--naming', 
                       choices=['original', 'hash', 'timestamp', 'sequential'],
                       default='original',
                       help='文件命名方法 (默认: original)')
    
    parser.add_argument('--post-slug', help='文章slug，用于文件名前缀')
    parser.add_argument('--no-post-slug', action='store_true', 
                       help='不使用文章slug前缀')
    
    # 下载选项
    parser.add_argument('--overwrite', action='store_true',
                       help='覆盖已存在的文件')
    parser.add_argument('--timeout', type=int, default=30,
                       help='下载超时时间(秒)')
    parser.add_argument('--delay', type=float, default=0.3,
                       help='请求间隔时间(秒)')
    
    # 请求头配置
    parser.add_argument('-r', '--referer', 
                       default='https://blog.csdn.net/',
                       help='Referer请求头 (默认: https://blog.csdn.net/)')
    parser.add_argument('--user-agent', 
                       default='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                       help='User-Agent请求头')
    
    # 配置文件
    parser.add_argument('-c', '--config', help='配置文件路径')
    parser.add_argument('--init-config', metavar='FILE',
                       help='生成配置文件模板')
    
    # 其他
    parser.add_argument('--no-backup', action='store_true',
                       help='不备份原始文件')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='详细输出模式')
    
    args = parser.parse_args()
    
    # 生成配置文件模板
    if args.init_config:
        config_template = {
            "md_file": "content/posts/my-article.md",
            "storage_dir": "static/assets/post_images",
            "md_path_prefix": "/assets/post_images",
            "naming_method": "sequential",
            "use_post_slug": True,
            "post_slug": "my-article",
            "overwrite_existing": false,
            "download_timeout": 30,
            "delay_between_requests": 0.3,
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "referer": "https://blog.csdn.net/",
            "backup_original": True,
            "verbose": False
        }
        
        with open(args.init_config, 'w', encoding='utf-8') as f:
            json.dump(config_template, f, indent=2, ensure_ascii=False)
        
        print(f"配置文件模板已生成: {args.init_config}")
        print("请修改配置后使用: python md_image_downloader.py -c {args.init_config} article.md")
        return
    
    # 准备配置参数
    config_kwargs = {
        'storage_dir': args.storage_dir,
        'md_path_prefix': args.path_prefix,
        'naming_method': args.naming,
        'use_post_slug': not args.no_post_slug,
        'post_slug': args.post_slug,
        'overwrite_existing': args.overwrite,
        'download_timeout': args.timeout,
        'delay_between_requests': args.delay,
        'referer': args.referer,
        'user_agent': args.user_agent,
        'backup_original': not args.no_backup,
        'verbose': args.verbose,
    }
    
    # 创建处理器
    processor = HugoImageProcessor(config_file=args.config, **config_kwargs)
    
    # 处理文件
    if args.md_file:
        processor.process_markdown(args.md_file)
    elif processor.config['md_file']:
        processor.process_markdown()
    else:
        print("错误: 请指定Markdown文件路径")
        parser.print_help()

if __name__ == "__main__":
    main()