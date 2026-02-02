+++
title = '人工智能中的数学基础'
date = 2026-02-02T14:33:33+08:00
draft = false
author = "simons"
categories = ["暂无"]
tags = ["暂无"]
description = "糟糕，写文章的时候忘记添加描述了！！！"
codeRunners = true #启用运行代码
cover = "https://cdn.pixabay.com/photo/2019/12/21/20/44/math-work-4711302_1280.jpg"

+++

## 1. 向量空间 (Vector Space)

### 数学概念

**向量空间**是线性代数的核心概念，它是一个满足特定运算规则的集合。

**定义要素**：
- **域 F**：通常是实数域 ℝ 或复数域 ℂ
- **向量集合 V**：非空集合
- **两种运算**：
  - 加法：V × V → V
  - 数乘：F × V → V

**八条公理详解**：

1. **加法交换律**：u + v = v + u
2. **加法结合律**：(u+v)+w = u+(v+w)
3. **加法单位元**：存在零向量 0
4. **加法逆元**：每个向量都有相反向量
5. **数乘结合律**：a(bv) = (ab)v
6. **数乘单位元**：1·v = v
7. **数乘对向量加法的分配律**：a(u+v) = au + av
8. **数乘对域加法的分配律**：(a+b)v = av + bv

### 在机器学习中的应用

- **特征向量**：每个数据样本可以表示为向量空间中的一个点
- **权重向量**：神经网络的权重形成向量空间
- **梯度下降**：在参数空间中进行优化

### Python实现

```python
import numpy as np
from typing import List, Union

class VectorSpace:
    """
    向量空间的实现
    这里我们实现 R^n 上的向量空间
    """
    
    def __init__(self, dimension: int):
        """
        初始化向量空间
        
        参数:
            dimension: 向量空间的维数
        """
        self.dimension = dimension
        self.zero_vector = np.zeros(dimension)
    
    def add(self, u: np.ndarray, v: np.ndarray) -> np.ndarray:
        """
        向量加法
        验证加法交换律: u + v = v + u
        """
        self._check_dimension(u)
        self._check_dimension(v)
        return u + v
    
    def scalar_multiply(self, scalar: float, v: np.ndarray) -> np.ndarray:
        """
        数乘运算
        """
        self._check_dimension(v)
        return scalar * v
    
    def additive_inverse(self, v: np.ndarray) -> np.ndarray:
        """
        加法逆元（相反向量）
        """
        self._check_dimension(v)
        return -v
    
    def _check_dimension(self, v: np.ndarray):
        """检查向量维度是否匹配"""
        if len(v) != self.dimension:
            raise ValueError(f"向量维度应为 {self.dimension}, 但得到 {len(v)}")
    
    def verify_axioms(self, u: np.ndarray, v: np.ndarray, w: np.ndarray, 
                     a: float, b: float) -> dict:
        """
        验证向量空间的八条公理
        
        返回:
            包含每条公理验证结果的字典
        """
        results = {}
        
        # 公理1: 加法交换律
        results['commutative'] = np.allclose(
            self.add(u, v), 
            self.add(v, u)
        )
        
        # 公理2: 加法结合律
        results['associative_add'] = np.allclose(
            self.add(self.add(u, v), w),
            self.add(u, self.add(v, w))
        )
        
        # 公理3: 加法单位元
        results['additive_identity'] = np.allclose(
            self.add(v, self.zero_vector),
            v
        )
        
        # 公理4: 加法逆元
        results['additive_inverse'] = np.allclose(
            self.add(v, self.additive_inverse(v)),
            self.zero_vector
        )
        
        # 公理5: 数乘结合律
        results['associative_scalar'] = np.allclose(
            self.scalar_multiply(a, self.scalar_multiply(b, v)),
            self.scalar_multiply(a * b, v)
        )
        
        # 公理6: 数乘单位元
        results['scalar_identity'] = np.allclose(
            self.scalar_multiply(1, v),
            v
        )
        
        # 公理7: 数乘对向量加法的分配律
        results['distributive_vector'] = np.allclose(
            self.scalar_multiply(a, self.add(u, v)),
            self.add(self.scalar_multiply(a, u), self.scalar_multiply(a, v))
        )
        
        # 公理8: 数乘对域加法的分配律
        results['distributive_scalar'] = np.allclose(
            self.scalar_multiply(a + b, v),
            self.add(self.scalar_multiply(a, v), self.scalar_multiply(b, v))
        )
        
        return results


# 示例使用
if __name__ == "__main__":
    # 创建3维向量空间
    V = VectorSpace(dimension=3)
    
    # 创建测试向量
    u = np.array([1.0, 2.0, 3.0])
    v = np.array([4.0, 5.0, 6.0])
    w = np.array([7.0, 8.0, 9.0])
    
    # 测试标量
    a, b = 2.0, 3.0
    
    print("=" * 50)
    print("向量空间公理验证")
    print("=" * 50)
    
    # 验证所有公理
    results = V.verify_axioms(u, v, w, a, b)
    
    for axiom, is_valid in results.items():
        print(f"{axiom:25s}: {'✓ 通过' if is_valid else '✗ 失败'}")
    
    print("\n" + "=" * 50)
    print("基本运算示例")
    print("=" * 50)
    
    print(f"u = {u}")
    print(f"v = {v}")
    print(f"u + v = {V.add(u, v)}")
    print(f"2 * u = {V.scalar_multiply(2, u)}")
    print(f"-v = {V.additive_inverse(v)}")
```

---

## 2. 线性组合 (Linear Combination)

### 数学概念

**线性组合**是向量空间中最基本的运算之一。

**定义**：给定向量 v₁, v₂, ..., vₖ 和标量 a₁, a₂, ..., aₖ，表达式：
$$a_1v_1 + a_2v_2 + ... + a_kv_k$$
称为这些向量的线性组合。

### 在机器学习中的应用

- **神经网络**：每个神经元的输出是输入的线性组合加上激活函数
- **线性回归**：预测值是特征的线性组合
- **PCA**：主成分是原始特征的线性组合

### Python实现

```python
class LinearCombination:
    """线性组合的实现"""
    
    @staticmethod
    def compute(vectors: List[np.ndarray], coefficients: List[float]) -> np.ndarray:
        """
        计算向量的线性组合
        
        参数:
            vectors: 向量列表 [v1, v2, ..., vk]
            coefficients: 系数列表 [a1, a2, ..., ak]
        
        返回:
            线性组合结果: a1*v1 + a2*v2 + ... + ak*vk
        """
        if len(vectors) != len(coefficients):
            raise ValueError("向量数量必须与系数数量相同")
        
        if not vectors:
            raise ValueError("至少需要一个向量")
        
        # 初始化结果为零向量
        result = np.zeros_like(vectors[0])
        
        # 累加每个向量的标量倍
        for coeff, vector in zip(coefficients, vectors):
            result += coeff * vector
        
        return result
    
    @staticmethod
    def matrix_form(vectors: List[np.ndarray], coefficients: np.ndarray) -> np.ndarray:
        """
        使用矩阵形式计算线性组合
        更高效的实现方式
        
        参数:
            vectors: 向量列表
            coefficients: 系数数组
        
        返回:
            线性组合结果
        """
        # 将向量列表转换为矩阵（每列是一个向量）
        matrix = np.column_stack(vectors)
        return matrix @ coefficients


# 示例：线性回归
class SimpleLinearRegression:
    """
    简单线性回归：使用线性组合进行预测
    y = w1*x1 + w2*x2 + ... + wn*xn + b
    """
    
    def __init__(self, n_features: int):
        self.n_features = n_features
        self.weights = None
        self.bias = None
    
    def fit(self, X: np.ndarray, y: np.ndarray):
        """
        使用最小二乘法拟合模型
        
        参数:
            X: 特征矩阵 (n_samples, n_features)
            y: 目标值 (n_samples,)
        """
        # 添加偏置项（在X前面添加一列1）
        X_with_bias = np.column_stack([np.ones(len(X)), X])
        
        # 最小二乘解: θ = (X^T X)^(-1) X^T y
        theta = np.linalg.inv(X_with_bias.T @ X_with_bias) @ X_with_bias.T @ y
        
        self.bias = theta[0]
        self.weights = theta[1:]
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        预测：计算特征的线性组合
        
        参数:
            X: 特征矩阵 (n_samples, n_features)
        
        返回:
            预测值 (n_samples,)
        """
        if self.weights is None:
            raise ValueError("模型尚未训练，请先调用 fit()")
        
        # y = X @ w + b (线性组合)
        return X @ self.weights + self.bias


# 示例使用
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("线性组合示例")
    print("=" * 50)
    
    # 示例1: 基本线性组合
    v1 = np.array([1, 0, 0])
    v2 = np.array([0, 1, 0])
    v3 = np.array([0, 0, 1])
    
    vectors = [v1, v2, v3]
    coefficients = [2, 3, 4]
    
    result = LinearCombination.compute(vectors, coefficients)
    print(f"2*v1 + 3*v2 + 4*v3 = {result}")
    
    # 示例2: 线性回归
    print("\n" + "=" * 50)
    print("线性回归示例（使用线性组合）")
    print("=" * 50)
    
    # 生成示例数据
    np.random.seed(42)
    X_train = np.random.randn(100, 3)  # 100个样本，3个特征
    true_weights = np.array([2.0, -1.0, 0.5])
    true_bias = 1.0
    y_train = X_train @ true_weights + true_bias + np.random.randn(100) * 0.1
    
    # 训练模型
    model = SimpleLinearRegression(n_features=3)
    model.fit(X_train, y_train)
    
    print(f"真实权重: {true_weights}")
    print(f"学习权重: {model.weights}")
    print(f"真实偏置: {true_bias}")
    print(f"学习偏置: {model.bias}")
    
    # 预测
    X_test = np.random.randn(5, 3)
    predictions = model.predict(X_test)
    print(f"\n测试样本预测: {predictions[:5]}")
```

---

## 3. 生成空间 (Span)

### 数学概念

**生成空间**（或张成空间）是由一组向量的所有线性组合构成的集合。

**定义**：
$$\text{Span}\{v_1, ..., v_k\} = \{a_1v_1 + ... + a_kv_k \mid a_1, ..., a_k \in F\}$$

**性质**：
- Span 是一个子空间
- 它是包含这些向量的最小子空间
- 如果向量组线性相关，移除某些向量不改变 Span

### 在机器学习中的应用

- **特征空间**：所有可能的特征向量构成的空间
- **列空间**：矩阵的列向量张成的空间（重要用于理解线性变换）
- **降维**：PCA 寻找能够张成数据主要变化方向的向量

### Python实现

```python
class Span:
    """生成空间的实现"""
    
    def __init__(self, vectors: List[np.ndarray]):
        """
        初始化生成空间
        
        参数:
            vectors: 生成该空间的向量列表
        """
        self.generators = [v.copy() for v in vectors]
        self.dimension = len(vectors[0]) if vectors else 0
        
        # 计算生成空间的基（通过行化简）
        self.basis = self._compute_basis()
    
    def _compute_basis(self) -> List[np.ndarray]:
        """
        使用行化简找到生成空间的一组基
        
        返回:
            基向量列表
        """
        if not self.generators:
            return []
        
        # 将向量组成矩阵（每行是一个向量）
        matrix = np.array(self.generators)
        
        # 使用QR分解找到线性无关的向量
        # 或使用行化简的方法
        return self._row_reduce_to_basis(matrix)
    
    def _row_reduce_to_basis(self, matrix: np.ndarray, tol: float = 1e-10) -> List[np.ndarray]:
        """
        通过行化简提取基向量
        
        参数:
            matrix: 向量矩阵（每行是一个向量）
            tol: 容差，用于判断是否为零
        
        返回:
            基向量列表
        """
        # 使用SVD找到秩和基
        U, s, Vt = np.linalg.svd(matrix, full_matrices=False)
        
        # 找到非零奇异值
        rank = np.sum(s > tol)
        
        # 提取对应的左奇异向量作为基
        # 实际上应该用原始向量的线性无关组合
        # 这里我们简化处理
        basis_vectors = []
        current_rank = 0
        
        for i, vec in enumerate(self.generators):
            if current_rank >= rank:
                break
            
            # 检查这个向量是否与已有基线性无关
            if not basis_vectors:
                basis_vectors.append(vec)
                current_rank += 1
            else:
                # 投影到已有基的正交补空间
                projection = vec.copy()
                for basis_vec in basis_vectors:
                    projection -= (np.dot(projection, basis_vec) / 
                                 np.dot(basis_vec, basis_vec)) * basis_vec
                
                if np.linalg.norm(projection) > tol:
                    basis_vectors.append(vec)
                    current_rank += 1
        
        return basis_vectors
    
    def contains(self, vector: np.ndarray, tol: float = 1e-10) -> bool:
        """
        判断向量是否在生成空间中
        
        参数:
            vector: 待检查的向量
            tol: 数值容差
        
        返回:
            True 如果向量在生成空间中
        """
        if not self.basis:
            return np.allclose(vector, 0, atol=tol)
        
        # 构造基矩阵
        basis_matrix = np.column_stack(self.basis)
        
        # 尝试求解 basis_matrix @ x = vector
        try:
            x, residuals, rank, s = np.linalg.lstsq(basis_matrix, vector, rcond=None)
            
            # 检查残差
            if len(residuals) > 0:
                return residuals[0] < tol
            else:
                # 如果方程恰好有解
                reconstruction = basis_matrix @ x
                return np.allclose(reconstruction, vector, atol=tol)
        except np.linalg.LinAlgError:
            return False
    
    def get_coordinates(self, vector: np.ndarray) -> Union[np.ndarray, None]:
        """
        获取向量在基下的坐标
        
        参数:
            vector: 向量
        
        返回:
            坐标数组，如果向量不在空间中则返回 None
        """
        if not self.contains(vector):
            return None
        
        basis_matrix = np.column_stack(self.basis)
        coordinates, _, _, _ = np.linalg.lstsq(basis_matrix, vector, rcond=None)
        
        return coordinates
    
    def get_dimension(self) -> int:
        """返回生成空间的维数"""
        return len(self.basis)


# 示例使用
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("生成空间示例")
    print("=" * 50)
    
    # 示例1: R^3 中的平面
    v1 = np.array([1.0, 0.0, 0.0])
    v2 = np.array([0.0, 1.0, 0.0])
    
    plane = Span([v1, v2])
    
    print(f"生成空间维数: {plane.get_dimension()}")
    print(f"基向量数量: {len(plane.basis)}")
    
    # 测试包含性
    test_vectors = [
        np.array([2.0, 3.0, 0.0]),  # 在平面内
        np.array([1.0, 1.0, 1.0]),  # 不在平面内
        np.array([0.0, 0.0, 0.0]),  # 零向量
    ]
    
    for i, vec in enumerate(test_vectors):
        in_span = plane.contains(vec)
        print(f"\n向量 {vec} 是否在生成空间中: {in_span}")
        if in_span:
            coords = plane.get_coordinates(vec)
            print(f"  坐标: {coords}")
    
    # 示例2: 线性相关的向量组
    print("\n" + "=" * 50)
    print("线性相关向量组的生成空间")
    print("=" * 50)
    
    u1 = np.array([1.0, 0.0, 0.0])
    u2 = np.array([0.0, 1.0, 0.0])
    u3 = np.array([2.0, 3.0, 0.0])  # u3 = 2*u1 + 3*u2 (线性相关)
    
    span_redundant = Span([u1, u2, u3])
    print(f"原始向量数: 3")
    print(f"生成空间维数: {span_redundant.get_dimension()}")
    print(f"基向量数量: {len(span_redundant.basis)}")
```

---

## 4. 欧几里得空间 (Euclidean Space)

### 数学概念

**欧几里得空间**是配备了内积（点积）的实向量空间，通常指 ℝⁿ。

**核心定义**：
1. **内积（点积）**：
   $$\mathbf{x} \cdot \mathbf{y} = \sum_{i=1}^n x_i y_i$$

2. **范数（长度）**：
   $$\|\mathbf{x}\| = \sqrt{\mathbf{x} \cdot \mathbf{x}} = \sqrt{\sum_{i=1}^n x_i^2}$$

3. **距离**：
   $$d(\mathbf{x}, \mathbf{y}) = \|\mathbf{x} - \mathbf{y}\|$$

**内积的性质**：
- 对称性：⟨x, y⟩ = ⟨y, x⟩
- 线性性：⟨ax + by, z⟩ = a⟨x, z⟩ + b⟨y, z⟩
- 正定性：⟨x, x⟩ ≥ 0，等号成立当且仅当 x = 0

### 在机器学习中的应用

- **相似度计算**：余弦相似度基于内积
- **距离度量**：欧氏距离用于聚类、KNN等
- **优化**：梯度是函数增长最快的方向（基于内积）
- **正则化**：L2正则化使用欧氏范数

### Python实现

```python
class EuclideanSpace:
    """欧几里得空间的实现"""
    
    def __init__(self, dimension: int):
        """
        初始化欧几里得空间
        
        参数:
            dimension: 空间维数
        """
        self.dimension = dimension
    
    def inner_product(self, x: np.ndarray, y: np.ndarray) -> float:
        """
        计算内积（点积）
        
        参数:
            x, y: 向量
        
        返回:
            内积 <x, y>
        """
        self._check_vectors(x, y)
        return np.dot(x, y)
    
    def norm(self, x: np.ndarray, p: int = 2) -> float:
        """
        计算向量的范数
        
        参数:
            x: 向量
            p: 范数的阶数 (1: L1, 2: L2, np.inf: L∞)
        
        返回:
            ||x||_p
        """
        self._check_dimension(x)
        return np.linalg.norm(x, ord=p)
    
    def distance(self, x: np.ndarray, y: np.ndarray) -> float:
        """
        计算欧氏距离
        
        参数:
            x, y: 向量
        
        返回:
            d(x, y) = ||x - y||
        """
        self._check_vectors(x, y)
        return self.norm(x - y)
    
    def angle(self, x: np.ndarray, y: np.ndarray) -> float:
        """
        计算两个向量之间的夹角（弧度）
        
        使用公式: cos(θ) = <x,y> / (||x|| ||y||)
        
        参数:
            x, y: 向量
        
        返回:
            夹角（弧度）
        """
        self._check_vectors(x, y)
        
        cos_angle = self.inner_product(x, y) / (self.norm(x) * self.norm(y))
        # 处理数值误差
        cos_angle = np.clip(cos_angle, -1.0, 1.0)
        
        return np.arccos(cos_angle)
    
    def cosine_similarity(self, x: np.ndarray, y: np.ndarray) -> float:
        """
        计算余弦相似度
        
        余弦相似度 = <x,y> / (||x|| ||y||)
        
        参数:
            x, y: 向量
        
        返回:
            余弦相似度 ∈ [-1, 1]
        """
        self._check_vectors(x, y)
        
        norm_x = self.norm(x)
        norm_y = self.norm(y)
        
        if norm_x == 0 or norm_y == 0:
            return 0.0
        
        return self.inner_product(x, y) / (norm_x * norm_y)
    
    def projection(self, x: np.ndarray, y: np.ndarray) -> np.ndarray:
        """
        计算 x 在 y 上的投影
        
        proj_y(x) = (<x,y> / <y,y>) * y
        
        参数:
            x: 被投影的向量
            y: 投影方向
        
        返回:
            投影向量
        """
        self._check_vectors(x, y)
        
        return (self.inner_product(x, y) / self.inner_product(y, y)) * y
    
    def gram_schmidt(self, vectors: List[np.ndarray]) -> List[np.ndarray]:
        """
        Gram-Schmidt 正交化过程
        
        将一组线性无关的向量转换为正交向量组
        
        参数:
            vectors: 向量列表
        
        返回:
            正交化后的向量列表
        """
        orthogonal = []
        
        for v in vectors:
            # 减去在所有已正交化向量上的投影
            w = v.copy()
            for u in orthogonal:
                w -= self.projection(v, u)
            
            # 只有非零向量才加入
            if self.norm(w) > 1e-10:
                orthogonal.append(w)
        
        return orthogonal
    
    def orthonormalize(self, vectors: List[np.ndarray]) -> List[np.ndarray]:
        """
        正交归一化：Gram-Schmidt + 归一化
        
        参数:
            vectors: 向量列表
        
        返回:
            标准正交基
        """
        orthogonal = self.gram_schmidt(vectors)
        
        # 归一化
        orthonormal = [v / self.norm(v) for v in orthogonal]
        
        return orthonormal
    
    def _check_dimension(self, x: np.ndarray):
        """检查向量维度"""
        if len(x) != self.dimension:
            raise ValueError(f"向量维度应为 {self.dimension}, 得到 {len(x)}")
    
    def _check_vectors(self, x: np.ndarray, y: np.ndarray):
        """检查两个向量的维度"""
        self._check_dimension(x)
        self._check_dimension(y)


# 机器学习应用示例
class KNearestNeighbors:
    """
    K近邻算法：基于欧氏距离
    """
    
    def __init__(self, k: int = 3):
        """
        初始化KNN分类器
        
        参数:
            k: 近邻数量
        """
        self.k = k
        self.X_train = None
        self.y_train = None
        self.euclidean_space = None
    
    def fit(self, X: np.ndarray, y: np.ndarray):
        """
        训练模型（存储训练数据）
        
        参数:
            X: 训练特征 (n_samples, n_features)
            y: 训练标签 (n_samples,)
        """
        self.X_train = X
        self.y_train = y
        self.euclidean_space = EuclideanSpace(X.shape[1])
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        预测
        
        参数:
            X: 测试特征 (n_samples, n_features)
        
        返回:
            预测标签 (n_samples,)
        """
        predictions = []
        
        for x in X:
            # 计算到所有训练样本的距离
            distances = [
                self.euclidean_space.distance(x, x_train)
                for x_train in self.X_train
            ]
            
            # 找到k个最近邻
            k_nearest_indices = np.argsort(distances)[:self.k]
            k_nearest_labels = self.y_train[k_nearest_indices]
            
            # 多数投票
            prediction = np.bincount(k_nearest_labels).argmax()
            predictions.append(prediction)
        
        return np.array(predictions)


# 示例使用
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("欧几里得空间示例")
    print("=" * 50)
    
    # 创建3维欧几里得空间
    E3 = EuclideanSpace(dimension=3)
    
    # 测试向量
    x = np.array([1.0, 2.0, 3.0])
    y = np.array([4.0, 5.0, 6.0])
    
    print(f"向量 x = {x}")
    print(f"向量 y = {y}")
    print(f"\n内积 <x, y> = {E3.inner_product(x, y):.4f}")
    print(f"||x|| = {E3.norm(x):.4f}")
    print(f"||y|| = {E3.norm(y):.4f}")
    print(f"距离 d(x, y) = {E3.distance(x, y):.4f}")
    print(f"夹角 θ = {np.degrees(E3.angle(x, y)):.2f}°")
    print(f"余弦相似度 = {E3.cosine_similarity(x, y):.4f}")
    
    # Gram-Schmidt 正交化示例
    print("\n" + "=" * 50)
    print("Gram-Schmidt 正交化")
    print("=" * 50)
    
    v1 = np.array([1.0, 1.0, 0.0])
    v2 = np.array([1.0, 0.0, 1.0])
    v3 = np.array([0.0, 1.0, 1.0])
    
    vectors = [v1, v2, v3]
    orthonormal_basis = E3.orthonormalize(vectors)
    
    print("原始向量:")
    for i, v in enumerate(vectors):
        print(f"  v{i+1} = {v}")
    
    print("\n标准正交基:")
    for i, v in enumerate(orthonormal_basis):
        print(f"  u{i+1} = {v}")
        print(f"  ||u{i+1}|| = {E3.norm(v):.6f}")
    
    # 验证正交性
    print("\n正交性验证:")
    for i in range(len(orthonormal_basis)):
        for j in range(i+1, len(orthonormal_basis)):
            dot_product = E3.inner_product(orthonormal_basis[i], orthonormal_basis[j])
            print(f"  <u{i+1}, u{j+1}> = {dot_product:.10f}")
    
    # KNN 示例
    print("\n" + "=" * 50)
    print("K近邻分类示例（基于欧氏距离）")
    print("=" * 50)
    
    # 生成示例数据
    np.random.seed(42)
    X_train = np.vstack([
        np.random.randn(50, 2) + [0, 0],  # 类别0
        np.random.randn(50, 2) + [3, 3],  # 类别1
    ])
    y_train = np.array([0]*50 + [1]*50)
    
    # 训练KNN
    knn = KNearestNeighbors(k=5)
    knn.fit(X_train, y_train)
    
    # 测试
    X_test = np.array([[0, 0], [3, 3], [1.5, 1.5]])
    predictions = knn.predict(X_test)
    
    print("测试样本预测:")
    for i, (sample, pred) in enumerate(zip(X_test, predictions)):
        print(f"  样本 {sample} → 类别 {pred}")
```

---

## 5. 线性无关 (Linear Independence)

### 数学概念

**线性无关**是线性代数中的核心概念，描述向量组之间的独立性。

**定义**：向量组 {v₁, v₂, ..., vₖ} 线性无关，当且仅当方程
$$a_1v_1 + a_2v_2 + ... + a_kv_k = 0$$
仅在 a₁ = a₂ = ... = aₖ = 0 时成立。

**等价条件**：
- 没有向量可以表示为其他向量的线性组合
- 从组中移除任何向量都会改变生成空间
- 矩阵的秩等于向量数量

### 在机器学习中的应用

- **特征选择**：去除线性相关的特征避免多重共线性
- **主成分分析**：寻找线性无关的主成分
- **矩阵分解**：确保分解的唯一性

### Python实现

```python
class LinearIndependence:
    """线性无关性检验和相关算法"""
    
    @staticmethod
    def is_linearly_independent(vectors: List[np.ndarray], tol: float = 1e-10) -> bool:
        """
        检查向量组是否线性无关
        
        方法：将向量组成矩阵，检查秩是否等于向量数量
        
        参数:
            vectors: 向量列表
            tol: 数值容差
        
        返回:
            True 如果向量组线性无关
        """
        if not vectors:
            return True
        
        # 构造矩阵（每列是一个向量）
        matrix = np.column_stack(vectors)
        
        # 计算秩
        rank = np.linalg.matrix_rank(matrix, tol=tol)
        
        # 如果秩等于向量数量，则线性无关
        return rank == len(vectors)
    
    @staticmethod
    def find_dependencies(vectors: List[np.ndarray], tol: float = 1e-10) -> dict:
        """
        找到线性相关关系
        
        参数:
            vectors: 向量列表
            tol: 数值容差
        
        返回:
            包含相关信息的字典
        """
        if not vectors:
            return {'is_independent': True, 'dependencies': []}
        
        matrix = np.column_stack(vectors)
        n_vectors = len(vectors)
        
        # 使用行化简
        # 首先做QR分解
        Q, R = np.linalg.qr(matrix)
        
        # 检查R的对角元素
        dependencies = []
        independent_indices = []
        
        for i in range(min(R.shape)):
            if abs(R[i, i]) > tol:
                independent_indices.append(i)
            else:
                # 找到这个向量与前面向量的关系
                if i > 0:
                    coeffs = R[:i, i] / np.diag(R[:i, :i])
                    dependencies.append({
                        'dependent_index': i,
                        'independent_indices': independent_indices.copy(),
                        'coefficients': coeffs
                    })
        
        return {
            'is_independent': len(dependencies) == 0,
            'rank': len(independent_indices),
            'independent_indices': independent_indices,
            'dependencies': dependencies
        }
    
    @staticmethod
    def extract_independent_subset(vectors: List[np.ndarray], tol: float = 1e-10) -> List[np.ndarray]:
        """
        提取最大线性无关子集
        
        参数:
            vectors: 向量列表
            tol: 数值容差
        
        返回:
            线性无关的向量子集
        """
        if not vectors:
            return []
        
        independent = []
        
        for v in vectors:
            # 检查加入这个向量后是否仍然线性无关
            test_set = independent + [v]
            if LinearIndependence.is_linearly_independent(test_set, tol):
                independent.append(v)
        
        return independent
    
    @staticmethod
    def compute_coefficients(target: np.ndarray, basis: List[np.ndarray]) -> Union[np.ndarray, None]:
        """
        如果 target 在 basis 的生成空间中，计算其系数
        
        参数:
            target: 目标向量
            basis: 基向量列表
        
        返回:
            系数数组，如果不在生成空间中则返回 None
        """
        if not basis:
            return None
        
        # 构造矩阵方程 basis_matrix @ coeffs = target
        basis_matrix = np.column_stack(basis)
        
        try:
            # 使用最小二乘求解
            coeffs, residuals, rank, s = np.linalg.lstsq(basis_matrix, target, rcond=None)
            
            # 检查是否有精确解
            reconstruction = basis_matrix @ coeffs
            if np.allclose(reconstruction, target, atol=1e-10):
                return coeffs
            else:
                return None
        except np.linalg.LinAlgError:
            return None


# 多重共线性检测（机器学习应用）
class MulticollinearityDetector:
    """
    检测特征之间的多重共线性
    多重共线性会导致线性回归不稳定
    """
    
    @staticmethod
    def compute_vif(X: np.ndarray, feature_idx: int) -> float:
        """
        计算方差膨胀因子 (Variance Inflation Factor, VIF)
        
        VIF_i = 1 / (1 - R²_i)
        其中 R²_i 是用其他特征预测第 i 个特征的决定系数
        
        VIF > 10 表示严重多重共线性
        
        参数:
            X: 特征矩阵 (n_samples, n_features)
            feature_idx: 要计算VIF的特征索引
        
        返回:
            VIF值
        """
        n_features = X.shape[1]
        
        # 选择其他特征作为自变量
        other_features = [i for i in range(n_features) if i != feature_idx]
        X_other = X[:, other_features]
        y = X[:, feature_idx]
        
        # 使用其他特征预测该特征
        # 计算 R²
        X_other_with_bias = np.column_stack([np.ones(len(X_other)), X_other])
        
        try:
            theta = np.linalg.inv(X_other_with_bias.T @ X_other_with_bias) @ X_other_with_bias.T @ y
            y_pred = X_other_with_bias @ theta
            
            # 计算 R²
            ss_res = np.sum((y - y_pred) ** 2)
            ss_tot = np.sum((y - np.mean(y)) ** 2)
            r_squared = 1 - (ss_res / ss_tot)
            
            # 计算 VIF
            if r_squared >= 0.9999:  # 防止除零
                return float('inf')
            
            vif = 1 / (1 - r_squared)
            return vif
            
        except np.linalg.LinAlgError:
            return float('inf')
    
    @staticmethod
    def detect_multicollinearity(X: np.ndarray, threshold: float = 10.0) -> dict:
        """
        检测所有特征的多重共线性
        
        参数:
            X: 特征矩阵
            threshold: VIF阈值
        
        返回:
            包含VIF和多重共线性诊断的字典
        """
        n_features = X.shape[1]
        vifs = []
        
        for i in range(n_features):
            vif = MulticollinearityDetector.compute_vif(X, i)
            vifs.append(vif)
        
        problematic_features = [i for i, vif in enumerate(vifs) if vif > threshold]
        
        return {
            'vifs': vifs,
            'problematic_features': problematic_features,
            'has_multicollinearity': len(problematic_features) > 0
        }


# 示例使用
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("线性无关性检验")
    print("=" * 50)
    
    # 示例1: 线性无关的向量组
    v1 = np.array([1.0, 0.0, 0.0])
    v2 = np.array([0.0, 1.0, 0.0])
    v3 = np.array([0.0, 0.0, 1.0])
    
    independent_vectors = [v1, v2, v3]
    
    is_indep = LinearIndependence.is_linearly_independent(independent_vectors)
    print(f"向量组 1:")
    for i, v in enumerate(independent_vectors):
        print(f"  v{i+1} = {v}")
    print(f"线性无关: {is_indep}")
    
    # 示例2: 线性相关的向量组
    print("\n" + "=" * 50)
    print("线性相关向量组")
    print("=" * 50)
    
    u1 = np.array([1.0, 2.0, 3.0])
    u2 = np.array([2.0, 4.0, 6.0])  # u2 = 2*u1
    u3 = np.array([3.0, 6.0, 9.0])  # u3 = 3*u1
    
    dependent_vectors = [u1, u2, u3]
    
    print(f"向量组 2:")
    for i, v in enumerate(dependent_vectors):
        print(f"  u{i+1} = {v}")
    
    dep_info = LinearIndependence.find_dependencies(dependent_vectors)
    print(f"\n线性无关: {dep_info['is_independent']}")
    print(f"秩: {dep_info['rank']}")
    print(f"独立向量索引: {dep_info['independent_indices']}")
    
    # 提取独立子集
    independent_subset = LinearIndependence.extract_independent_subset(dependent_vectors)
    print(f"\n最大线性无关子集大小: {len(independent_subset)}")
    
    # 示例3: 多重共线性检测
    print("\n" + "=" * 50)
    print("多重共线性检测（机器学习应用）")
    print("=" * 50)
    
    # 创建有多重共线性的数据
    np.random.seed(42)
    n_samples = 100
    
    X1 = np.random.randn(n_samples)
    X2 = np.random.randn(n_samples)
    X3 = 2 * X1 + 3 * X2 + np.random.randn(n_samples) * 0.1  # X3 几乎是 X1 和 X2 的线性组合
    
    X = np.column_stack([X1, X2, X3])
    
    multicollinearity = MulticollinearityDetector.detect_multicollinearity(X)
    
    print("各特征的 VIF:")
    for i, vif in enumerate(multicollinearity['vifs']):
        print(f"  特征 {i}: VIF = {vif:.2f}")
    
    if multicollinearity['has_multicollinearity']:
        print(f"\n警告: 检测到多重共线性!")
        print(f"问题特征索引: {multicollinearity['problematic_features']}")
    else:
        print("\n未检测到严重的多重共线性")
```

继续第二部分...

---

## 6. 基 (Basis)

### 数学概念

**基**是向量空间中最重要的概念之一，它提供了空间的"坐标系统"。

**定义**：向量空间 V 的一个基 B = {v₁, v₂, ..., vₙ} 满足两个条件：
1. **线性无关**：基中的向量线性无关
2. **生成整个空间**：Span(B) = V

**重要性质**：
- 每个向量在给定基下有唯一的坐标表示
- 同一空间的所有基都有相同数量的向量
- 基的选择影响计算的复杂度和数值稳定性

### 在机器学习中的应用

- **特征表示**：选择合适的基可以简化问题
- **PCA**：找到数据方差最大的正交基
- **傅里叶变换**：从时域基转换到频域基
- **小波变换**：多尺度基表示

### Python实现

```python
class Basis:
    """基的表示和操作"""
    
    def __init__(self, vectors: List[np.ndarray], name: str = "B"):
        """
        初始化基
        
        参数:
            vectors: 基向量列表
            name: 基的名称
        """
        # 验证是否线性无关
        if not LinearIndependence.is_linearly_independent(vectors):
            raise ValueError("基向量必须线性无关")
        
        self.vectors = [v.copy() for v in vectors]
        self.dimension = len(vectors)
        self.name = name
        
        # 构造基矩阵（每列是一个基向量）
        self.matrix = np.column_stack(vectors)
        
        # 计算逆矩阵（用于坐标变换）
        try:
            self.inverse_matrix = np.linalg.inv(self.matrix)
        except np.linalg.LinAlgError:
            self.inverse_matrix = None
    
    def to_coordinates(self, vector: np.ndarray) -> np.ndarray:
        """
        将向量转换为该基下的坐标
        
        如果 v = c₁v₁ + c₂v₂ + ... + cₙvₙ
        则返回 [c₁, c₂, ..., cₙ]
        
        参数:
            vector: 向量（标准基下）
        
        返回:
            该基下的坐标
        """
        if self.inverse_matrix is None:
            raise ValueError("基不可逆")
        
        return self.inverse_matrix @ vector
    
    def from_coordinates(self, coordinates: np.ndarray) -> np.ndarray:
        """
        从该基下的坐标转换为标准表示
        
        参数:
            coordinates: 该基下的坐标 [c₁, c₂, ..., cₙ]
        
        返回:
            向量（标准基下）
        """
        return self.matrix @ coordinates
    
    def change_of_basis_matrix(self, other_basis: 'Basis') -> np.ndarray:
        """
        计算从this基到other基的变换矩阵
        
        参数:
            other_basis: 目标基
        
        返回:
            变换矩阵 P，使得 [v]_other = P [v]_this
        """
        if self.inverse_matrix is None:
            raise ValueError("当前基不可逆")
        
        # P = B_other^(-1) @ B_this
        return other_basis.inverse_matrix @ self.matrix
    
    def is_orthogonal(self, tol: float = 1e-10) -> bool:
        """
        检查是否为正交基
        
        参数:
            tol: 数值容差
        
        返回:
            True 如果是正交基
        """
        n = len(self.vectors)
        
        for i in range(n):
            for j in range(i+1, n):
                dot_product = np.dot(self.vectors[i], self.vectors[j])
                if abs(dot_product) > tol:
                    return False
        
        return True
    
    def is_orthonormal(self, tol: float = 1e-10) -> bool:
        """
        检查是否为标准正交基
        
        参数:
            tol: 数值容差
        
        返回:
            True 如果是标准正交基
        """
        if not self.is_orthogonal(tol):
            return False
        
        # 检查每个向量的范数是否为1
        for v in self.vectors:
            if abs(np.linalg.norm(v) - 1.0) > tol:
                return False
        
        return True
    
    def orthonormalize(self) -> 'Basis':
        """
        使用Gram-Schmidt过程将基正交归一化
        
        返回:
            新的标准正交基
        """
        E3 = EuclideanSpace(self.dimension)
        orthonormal_vectors = E3.orthonormalize(self.vectors)
        
        return Basis(orthonormal_vectors, name=f"{self.name}_orthonormal")


class PrincipalComponentAnalysis:
    """
    主成分分析 (PCA) - 寻找数据的最优基
    
    PCA 找到使数据方差最大的正交基
    """
    
    def __init__(self, n_components: int):
        """
        初始化PCA
        
        参数:
            n_components: 主成分数量
        """
        self.n_components = n_components
        self.components = None  # 主成分（新的基）
        self.mean = None
        self.explained_variance = None
        self.explained_variance_ratio = None
    
    def fit(self, X: np.ndarray):
        """
        拟合PCA模型
        
        参数:
            X: 数据矩阵 (n_samples, n_features)
        """
        # 中心化数据
        self.mean = np.mean(X, axis=0)
        X_centered = X - self.mean
        
        # 计算协方差矩阵
        cov_matrix = (X_centered.T @ X_centered) / (len(X) - 1)
        
        # 特征值分解
        eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
        
        # 按特征值降序排序
        idx = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[idx]
        eigenvectors = eigenvectors[:, idx]
        
        # 选择前n_components个主成分
        self.components = eigenvectors[:, :self.n_components].T
        self.explained_variance = eigenvalues[:self.n_components]
        self.explained_variance_ratio = self.explained_variance / np.sum(eigenvalues)
    
    def transform(self, X: np.ndarray) -> np.ndarray:
        """
        将数据转换到主成分空间
        
        参数:
            X: 数据矩阵 (n_samples, n_features)
        
        返回:
            转换后的数据 (n_samples, n_components)
        """
        if self.components is None:
            raise ValueError("模型尚未拟合")
        
        X_centered = X - self.mean
        return X_centered @ self.components.T
    
    def inverse_transform(self, X_transformed: np.ndarray) -> np.ndarray:
        """
        从主成分空间转换回原始空间
        
        参数:
            X_transformed: 主成分空间的数据 (n_samples, n_components)
        
        返回:
            原始空间的近似重构 (n_samples, n_features)
        """
        if self.components is None:
            raise ValueError("模型尚未拟合")
        
        return X_transformed @ self.components + self.mean


# 示例使用
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("基的操作示例")
    print("=" * 50)
    
    # 示例1: 标准基
    e1 = np.array([1.0, 0.0, 0.0])
    e2 = np.array([0.0, 1.0, 0.0])
    e3 = np.array([0.0, 0.0, 1.0])
    
    standard_basis = Basis([e1, e2, e3], name="Standard")
    
    print("标准基:")
    for i, v in enumerate(standard_basis.vectors):
        print(f"  e{i+1} = {v}")
    
    print(f"是否正交: {standard_basis.is_orthogonal()}")
    print(f"是否标准正交: {standard_basis.is_orthonormal()}")
    
    # 示例2: 自定义基和坐标变换
    print("\n" + "=" * 50)
    print("坐标变换")
    print("=" * 50)
    
    # 定义一个新基
    b1 = np.array([1.0, 1.0, 0.0])
    b2 = np.array([1.0, 0.0, 1.0])
    b3 = np.array([0.0, 1.0, 1.0])
    
    custom_basis = Basis([b1, b2, b3], name="Custom")
    
    # 测试向量
    v = np.array([3.0, 4.0, 5.0])
    
    print(f"向量 v（标准基）= {v}")
    
    # 转换到自定义基
    coords_custom = custom_basis.to_coordinates(v)
    print(f"v 在自定义基下的坐标 = {coords_custom}")
    
    # 验证：从坐标转换回来
    v_reconstructed = custom_basis.from_coordinates(coords_custom)
    print(f"重构的 v = {v_reconstructed}")
    print(f"重构误差 = {np.linalg.norm(v - v_reconstructed):.10f}")
    
    # 基变换矩阵
    print("\n" + "=" * 50)
    print("基变换")
    print("=" * 50)
    
    P = custom_basis.change_of_basis_matrix(standard_basis)
    print("从自定义基到标准基的变换矩阵 P:")
    print(P)
    
    # 示例3: 正交化
    print("\n" + "=" * 50)
    print("基的正交化")
    print("=" * 50)
    
    orthonormal_basis = custom_basis.orthonormalize()
    
    print("正交归一化后的基:")
    for i, v in enumerate(orthonormal_basis.vectors):
        print(f"  u{i+1} = {v}")
        print(f"  ||u{i+1}|| = {np.linalg.norm(v):.6f}")
    
    print(f"\n是否标准正交: {orthonormal_basis.is_orthonormal()}")
    
    # 示例4: PCA（找到数据的最优基）
    print("\n" + "=" * 50)
    print("主成分分析 (PCA) - 数据驱动的基选择")
    print("=" * 50)
    
    # 生成示例数据（椭圆分布）
    np.random.seed(42)
    n_samples = 300
    
    # 在主轴方向生成数据
    data_pca = np.random.randn(n_samples, 2)
    data_pca[:, 0] *= 3  # 第一个方向方差更大
    data_pca[:, 1] *= 1
    
    # 旋转数据
    theta = np.pi / 4
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])
    data_pca = data_pca @ rotation_matrix.T
    
    # 应用PCA
    pca = PrincipalComponentAnalysis(n_components=2)
    pca.fit(data_pca)
    
    print("主成分（新的基向量）:")
    for i, component in enumerate(pca.components):
        print(f"  PC{i+1} = {component}")
    
    print(f"\n解释方差比: {pca.explained_variance_ratio}")
    print(f"累积解释方差比: {np.cumsum(pca.explained_variance_ratio)}")
    
    # 转换数据
    data_transformed = pca.transform(data_pca)
    print(f"\n原始数据形状: {data_pca.shape}")
    print(f"转换后数据形状: {data_transformed.shape}")
    
    # 重构
    data_reconstructed = pca.inverse_transform(data_transformed)
    reconstruction_error = np.mean(np.linalg.norm(data_pca - data_reconstructed, axis=1))
    print(f"重构误差: {reconstruction_error:.10f}")
```

---

## 7. 维数 (Dimension)

### 数学概念

**维数**是向量空间最基本的不变量，描述空间的"自由度"。

**定义**：如果向量空间 V 有一个有限基，则所有基的向量个数相同，这个数称为 V 的维数，记作 dim(V)。

**重要定理**：
1. **维数定理**：所有基的大小相同
2. **秩-零化度定理**：对于线性变换 T: V → W，
   dim(V) = rank(T) + nullity(T)

### 在机器学习中的应用

- **维度灾难**：高维空间中数据稀疏
- **降维**：PCA, t-SNE 等减少维数
- **嵌入**：Word2Vec 将词映射到低维空间
- **流形学习**：发现数据的内在维度

### Python实现

```python
class DimensionAnalysis:
    """维数分析和相关概念"""
    
    @staticmethod
    def compute_dimension(vectors: List[np.ndarray]) -> int:
        """
        计算向量组生成空间的维数
        
        维数 = 秩 = 最大线性无关子集的大小
        
        参数:
            vectors: 向量列表
        
        返回:
            维数
        """
        if not vectors:
            return 0
        
        matrix = np.column_stack(vectors)
        return np.linalg.matrix_rank(matrix)
    
    @staticmethod
    def intrinsic_dimension_mle(X: np.ndarray, k: int = 10) -> float:
        """
        使用最大似然估计估计数据的内在维度
        
        基于局部距离的方法
        
        参数:
            X: 数据矩阵 (n_samples, n_features)
            k: 近邻数量
        
        返回:
            估计的内在维度
        """
        from scipy.spatial.distance import cdist
        
        n_samples = len(X)
        
        # 计算距离矩阵
        distances = cdist(X, X)
        
        # 对每个点，找到k个最近邻
        dimensions = []
        
        for i in range(n_samples):
            # 获取第i个点到其他点的距离
            dists = distances[i]
            
            # 排序并选择最近的k+1个点（包括自己）
            nearest_indices = np.argsort(dists)[1:k+2]  # 跳过自己
            nearest_dists = dists[nearest_indices]
            
            # 使用MLE估计局部维度
            # d ≈ (k-1) / sum(log(r_k / r_i))
            r_k = nearest_dists[-1]
            
            if r_k > 1e-10:
                log_ratios = np.log(r_k / nearest_dists[:-1])
                local_dim = (k - 1) / np.sum(log_ratios)
                dimensions.append(local_dim)
        
        return np.median(dimensions)


class DimensionalityCurse:
    """
    维度灾难的演示
    """
    
    @staticmethod
    def volume_of_unit_sphere(dimension: int) -> float:
        """
        计算单位球的体积
        
        V_d = π^(d/2) / Γ(d/2 + 1)
        
        参数:
            dimension: 维数
        
        返回:
            单位球体积
        """
        from scipy.special import gamma
        
        return np.pi ** (dimension / 2) / gamma(dimension / 2 + 1)
    
    @staticmethod
    def sample_density(n_samples: int, dimension: int) -> float:
        """
        计算给定样本数和维度下的样本密度
        
        参数:
            n_samples: 样本数量
            dimension: 空间维数
        
        返回:
            样本密度（样本/体积）
        """
        # 假设数据在单位超立方体中
        volume = 1.0  # 单位超立方体体积总是1
        
        return n_samples / volume
    
    @staticmethod
    def nearest_neighbor_distance(n_samples: int, dimension: int) -> float:
        """
        估计最近邻的平均距离
        
        在高维空间中，最近邻距离增加
        
        参数:
            n_samples: 样本数量
            dimension: 空间维数
        
        返回:
            估计的最近邻距离
        """
        # 简化估计：d ∝ (V/n)^(1/d)
        # 其中 V 是体积，n 是样本数
        
        return (1.0 / n_samples) ** (1.0 / dimension)


# 示例使用
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("维数计算")
    print("=" * 50)
    
    # 示例1: 计算生成空间的维数
    v1 = np.array([1, 0, 0, 0])
    v2 = np.array([0, 1, 0, 0])
    v3 = np.array([1, 1, 0, 0])  # 线性相关
    v4 = np.array([0, 0, 1, 0])
    
    vectors = [v1, v2, v3, v4]
    dim = DimensionAnalysis.compute_dimension(vectors)
    
    print(f"向量数量: {len(vectors)}")
    print(f"生成空间的维数: {dim}")
    
    # 示例2: 内在维度估计
    print("\n" + "=" * 50)
    print("内在维度估计")
    print("=" * 50)
    
    # 生成嵌入在高维空间中的低维数据
    np.random.seed(42)
    n_samples = 500
    
    # 真实的2D数据
    t = np.random.rand(n_samples) * 2 * np.pi
    true_2d = np.column_stack([np.cos(t), np.sin(t)])
    
    # 嵌入到10D空间
    embedding_matrix = np.random.randn(2, 10)
    embedded_data = true_2d @ embedding_matrix
    
    print(f"嵌入空间维数: {embedded_data.shape[1]}")
    
    estimated_dim = DimensionAnalysis.intrinsic_dimension_mle(embedded_data, k=15)
    print(f"估计的内在维度: {estimated_dim:.2f}")
    print(f"真实的内在维度: 2")
    
    # 示例3: 维度灾难
    print("\n" + "=" * 50)
    print("维度灾难演示")
    print("=" * 50)
    
    n_samples = 1000
    dimensions = [2, 5, 10, 20, 50, 100]
    
    print(f"固定样本数: {n_samples}\n")
    print(f"{'维数':>6} | {'单位球体积':>15} | {'最近邻距离':>15}")
    print("-" * 50)
    
    for d in dimensions:
        volume = DimensionalityCurse.volume_of_unit_sphere(d)
        nn_dist = DimensionalityCurse.nearest_neighbor_distance(n_samples, d)
        
        print(f"{d:6d} | {volume:15.6e} | {nn_dist:15.6f}")
    
    print("\n观察:")
    print("1. 单位球体积先增后减（高维时趋近于0）")
    print("2. 最近邻距离随维度增加而增大")
    print("3. 高维空间中数据变得稀疏")
```

---

## 8. 标准基 (Standard Basis)

### 数学概念

**标准基**是 Fⁿ 中最自然、最常用的基。

**定义**：对于 n 维坐标空间，标准基是：
$$e_1 = (1, 0, ..., 0), e_2 = (0, 1, ..., 0), ..., e_n = (0, 0, ..., 1)$$

**性质**：
- 标准正交基
- 坐标表示最简单
- 计算效率最高

### Python实现

```python
class StandardBasis:
    """标准基的实现和应用"""
    
    def __init__(self, dimension: int):
        """
        创建标准基
        
        参数:
            dimension: 维数
        """
        self.dimension = dimension
        self.vectors = self._create_standard_basis()
        self.basis = Basis(self.vectors, name="Standard")
    
    def _create_standard_basis(self) -> List[np.ndarray]:
        """
        创建标准基向量
        
        返回:
            标准基向量列表
        """
        basis_vectors = []
        
        for i in range(self.dimension):
            e = np.zeros(self.dimension)
            e[i] = 1.0
            basis_vectors.append(e)
        
        return basis_vectors
    
    def get_vector(self, index: int) -> np.ndarray:
        """
        获取第 i 个标准基向量
        
        参数:
            index: 索引（从0开始）
        
        返回:
            第 i 个标准基向量
        """
        if index < 0 or index >= self.dimension:
            raise IndexError(f"索引应在 [0, {self.dimension}) 范围内")
        
        return self.vectors[index].copy()


# 示例使用
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("标准基")
    print("=" * 50)
    
    # 创建3维标准基
    std_basis_3d = StandardBasis(dimension=3)
    
    print("3维标准基:")
    for i in range(std_basis_3d.dimension):
        e = std_basis_3d.get_vector(i)
        print(f"  e_{i+1} = {e}")
    
    # 验证性质
    print(f"\n是否标准正交: {std_basis_3d.basis.is_orthonormal()}")
    
    # 任意向量在标准基下的坐标就是其分量
    v = np.array([3.0, 4.0, 5.0])
    coords = std_basis_3d.basis.to_coordinates(v)
    
    print(f"\n向量 v = {v}")
    print(f"在标准基下的坐标 = {coords}")
    print(f"坐标与分量相同: {np.allclose(v, coords)}")
```

---

## 9. 范数 (Norm)

### 数学概念

**范数**是向量"长度"的推广，用于度量向量的大小。

**定义**：函数 ∥·∥: V → ℝ 称为范数，如果满足：
1. **正定性**：∥v∥ ≥ 0，且 ∥v∥ = 0 ⟺ v = 0
2. **齐次性**：∥αv∥ = |α|∥v∥
3. **三角不等式**：∥u + v∥ ≤ ∥u∥ + ∥v∥

**常用范数**：
- **L¹ 范数**（曼哈顿距离）：∥x∥₁ = Σ|xᵢ|
- **L² 范数**（欧氏距离）：∥x∥₂ = √(Σxᵢ²)
- **L∞ 范数**（最大范数）：∥x∥∞ = max|xᵢ|
- **Lᵖ 范数**：∥x∥ₚ = (Σ|xᵢ|ᵖ)^(1/p)

### 在机器学习中的应用

- **正则化**：L1正则化（Lasso）、L2正则化（Ridge）
- **距离度量**：不同范数对应不同的距离概念
- **优化**：梯度的范数用于判断收敛
- **归一化**：特征缩放

### Python实现

```python
class NormOperations:
    """各种范数的计算和应用"""
    
    @staticmethod
    def lp_norm(x: np.ndarray, p: float = 2) -> float:
        """
        计算 Lp 范数
        
        ||x||_p = (Σ|x_i|^p)^(1/p)
        
        参数:
            x: 向量
            p: 范数的阶数
        
        返回:
            Lp 范数
        """
        if p == np.inf:
            return np.max(np.abs(x))
        elif p == 1:
            return np.sum(np.abs(x))
        elif p == 2:
            return np.sqrt(np.sum(x ** 2))
        else:
            return np.sum(np.abs(x) ** p) ** (1.0 / p)
    
    @staticmethod
    def normalize(x: np.ndarray, p: float = 2) -> np.ndarray:
        """
        归一化向量（使其范数为1）
        
        参数:
            x: 向量
            p: 使用的范数
        
        返回:
            归一化后的向量
        """
        norm = NormOperations.lp_norm(x, p)
        
        if norm < 1e-10:
            return x
        
        return x / norm
    
    @staticmethod
    def unit_ball_visualization_2d(p_values: List[float] = [0.5, 1, 2, np.inf]):
        """
        可视化不同范数的单位球（2D情况）
        
        参数:
            p_values: 要可视化的p值列表
        """
        import matplotlib.pyplot as plt
        
        fig, axes = plt.subplots(2, 2, figsize=(12, 12))
        axes = axes.ravel()
        
        theta = np.linspace(0, 2*np.pi, 1000)
        
        for idx, p in enumerate(p_values):
            ax = axes[idx]
            
            if p == np.inf:
                # L∞ 范数：正方形
                x = np.array([1, 1, -1, -1, 1])
                y = np.array([1, -1, -1, 1, 1])
            else:
                # 参数方程
                x = np.sign(np.cos(theta)) * np.abs(np.cos(theta)) ** (2/p)
                y = np.sign(np.sin(theta)) * np.abs(np.sin(theta)) ** (2/p)
            
            ax.plot(x, y, 'b-', linewidth=2)
            ax.grid(True, alpha=0.3)
            ax.set_aspect('equal')
            ax.set_xlim(-1.5, 1.5)
            ax.set_ylim(-1.5, 1.5)
            ax.set_title(f'L{p} Norm Unit Ball', fontsize=14)
            ax.axhline(y=0, color='k', linewidth=0.5)
            ax.axvline(x=0, color='k', linewidth=0.5)
        
        plt.tight_layout()
        return fig


class RegularizedLinearRegression:
    """
    带正则化的线性回归
    
    损失函数：L(w) = ||Xw - y||² + λ||w||ₚ
    """
    
    def __init__(self, regularization: str = 'l2', lambda_reg: float = 0.1):
        """
        初始化正则化线性回归
        
        参数:
            regularization: 'l1' (Lasso), 'l2' (Ridge), 或 'none'
            lambda_reg: 正则化强度
        """
        self.regularization = regularization
        self.lambda_reg = lambda_reg
        self.weights = None
        self.bias = None
    
    def fit(self, X: np.ndarray, y: np.ndarray, max_iter: int = 1000, lr: float = 0.01):
        """
        使用梯度下降训练模型
        
        参数:
            X: 特征矩阵 (n_samples, n_features)
            y: 目标值 (n_samples,)
            max_iter: 最大迭代次数
            lr: 学习率
        """
        n_samples, n_features = X.shape
        
        # 初始化权重
        self.weights = np.zeros(n_features)
        self.bias = 0.0
        
        for iteration in range(max_iter):
            # 预测
            y_pred = X @ self.weights + self.bias
            
            # 计算梯度
            error = y_pred - y
            grad_w = (2/n_samples) * (X.T @ error)
            grad_b = (2/n_samples) * np.sum(error)
            
            # 添加正则化项的梯度
            if self.regularization == 'l2':
                grad_w += 2 * self.lambda_reg * self.weights
            elif self.regularization == 'l1':
                grad_w += self.lambda_reg * np.sign(self.weights)
            
            # 更新参数
            self.weights -= lr * grad_w
            self.bias -= lr * grad_b
            
            # 每100次迭代打印损失
            if iteration % 100 == 0:
                loss = self._compute_loss(X, y)
                print(f"Iteration {iteration}: Loss = {loss:.4f}")
    
    def _compute_loss(self, X: np.ndarray, y: np.ndarray) -> float:
        """计算损失函数"""
        y_pred = X @ self.weights + self.bias
        mse = np.mean((y - y_pred) ** 2)
        
        if self.regularization == 'l2':
            reg_term = self.lambda_reg * np.sum(self.weights ** 2)
        elif self.regularization == 'l1':
            reg_term = self.lambda_reg * np.sum(np.abs(self.weights))
        else:
            reg_term = 0
        
        return mse + reg_term
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """预测"""
        return X @ self.weights + self.bias


# 示例使用
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("范数计算")
    print("=" * 50)
    
    # 示例向量
    x = np.array([3, 4, 0])
    
    print(f"向量 x = {x}\n")
    
    # 计算不同范数
    for p in [1, 2, 3, np.inf]:
        norm_value = NormOperations.lp_norm(x, p)
        print(f"L{p} 范数: ||x||_{p} = {norm_value:.4f}")
    
    # 归一化
    print("\n" + "=" * 50)
    print("向量归一化")
    print("=" * 50)
    
    for p in [1, 2, np.inf]:
        x_normalized = NormOperations.normalize(x, p)
        norm_check = NormOperations.lp_norm(x_normalized, p)
        
        print(f"\nL{p} 归一化:")
        print(f"  归一化向量: {x_normalized}")
        print(f"  验证范数 = {norm_check:.10f}")
    
    # 正则化线性回归示例
    print("\n" + "=" * 50)
    print("正则化线性回归（范数应用）")
    print("=" * 50)
    
    # 生成数据
    np.random.seed(42)
    n_samples, n_features = 100, 5
    X_train = np.random.randn(n_samples, n_features)
    true_weights = np.array([2, -1, 0, 0, 0.5])  # 稀疏权重
    y_train = X_train @ true_weights + np.random.randn(n_samples) * 0.1
    
    print(f"真实权重: {true_weights}\n")
    
    # L2 正则化 (Ridge)
    print("L2 正则化 (Ridge):")
    ridge = RegularizedLinearRegression(regularization='l2', lambda_reg=0.1)
    ridge.fit(X_train, y_train, max_iter=500, lr=0.01)
    print(f"学习的权重: {ridge.weights}")
    print(f"||w||_2 = {NormOperations.lp_norm(ridge.weights, 2):.4f}\n")
    
    # L1 正则化 (Lasso)
    print("L1 正则化 (Lasso):")
    lasso = RegularizedLinearRegression(regularization='l1', lambda_reg=0.1)
    lasso.fit(X_train, y_train, max_iter=500, lr=0.01)
    print(f"学习的权重: {lasso.weights}")
    print(f"||w||_1 = {NormOperations.lp_norm(lasso.weights, 1):.4f}")
    print(f"稀疏性（接近0的权重数）: {np.sum(np.abs(lasso.weights) < 0.1)}")
```
