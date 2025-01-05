+++
date = '2024-12-29T09:31:37+08:00'
draft = false
title = 'Go 最佳实践'
toc = true
+++



在 Go 项目架构中，有一些重要的设计原则和规则。我来详细说明：

1. 接口定义规则：
```go
// ✅ 正确：接口定义在使用方(调用方)包中
package handler
type UserService interface {
    Create(ctx context.Context, user *User) error
}

// ❌ 错误：接口定义在实现方包中
package service
type UserService interface {
    Create(ctx context.Context, user *User) error
}
```

2. 依赖方向：
```go
// ✅ 正确的依赖方向
handler -> service -> repository -> database

// ❌ 错误：不应该出现反向依赖
service -> handler
repository -> service
```

3. 数据模型定义：
```go
// ✅ 正确：每层使用自己的数据模型
package handler
type CreateUserRequest struct {  // API层模型
    Username string `json:"username"`
}

package service
type UserDTO struct {  // 业务层模型
    ID       uint64
    Username string
}

package repository
type UserDO struct {  // 数据层模型
    ID        uint64 `gorm:"primaryKey"`
    Username  string
    CreatedAt time.Time
}

// ❌ 错误：直接在所有层使用相同的模型
type User struct {
    ID        uint64 `json:"id" gorm:"primaryKey"`
    Username  string `json:"username"`
    CreatedAt time.Time `json:"created_at"`
}
```

4. 错误处理层级：
```go
// ✅ 正确：每层对错误进行适当包装
package repository
func (r *UserRepo) Create(user *UserDO) error {
    return fmt.Errorf("database error: %w", err)
}

package service
func (s *UserService) Create(user *UserDTO) error {
    return fmt.Errorf("business error: %w", err)
}

package handler
func (h *UserHandler) Create(c *gin.Context) {
    if err := h.service.Create(user); err != nil {
        c.JSON(getErrorStatus(err), ErrorResponse{err.Error()})
        return
    }
}

// ❌ 错误：直接暴露底层错误
if err := db.Create(&user).Error; err != nil {
    c.JSON(500, err.Error())
}
```

5. 包的组织：
```
✅ 正确的包组织：
project/
  ├── api/
  │   └── handler/       # HTTP 处理层
  ├── internal/
  │   ├── service/      # 业务逻辑层
  │   ├── repository/   # 数据访问层
  │   └── model/        # 内部数据模型
  ├── pkg/
  │   └── util/         # 公共工具函数
  └── main.go

❌ 错误的包组织：
project/
  ├── handlers/
  ├── services/
  ├── models/
  └── main.go
```

6. 依赖注入：
```go
// ✅ 正确：通过构造函数注入依赖
func NewUserHandler(service UserService) *UserHandler {
    return &UserHandler{service: service}
}

// ❌ 错误：全局变量或直接初始化
var userService = &UserService{}
```

7. 接口隔离：
```go
// ✅ 正确：小接口，职责单一
type UserReader interface {
    GetUser(id uint64) (*User, error)
}

type UserWriter interface {
    CreateUser(user *User) error
}

// ❌ 错误：大接口，职责过多
type UserService interface {
    GetUser(id uint64) (*User, error)
    CreateUser(user *User) error
    UpdateUser(user *User) error
    DeleteUser(id uint64) error
    ListUsers() ([]*User, error)
    SearchUsers(query string) ([]*User, error)
}
```

8. 配置管理：
```go
// ✅ 正确：集中管理配置
package config

type Config struct {
    Server ServerConfig
    DB     DatabaseConfig
    Redis  RedisConfig
}

// ❌ 错误：分散的配置或硬编码
var serverPort = 8080
var dbConnection = "root:password@tcp(localhost:3306)/db"
```

9. 上下文传递：
```go
// ✅ 正确：统一使用 context 传递请求上下文
func (h *Handler) Create(c *gin.Context) {
    ctx := c.Request.Context()
    err := h.service.Create(ctx, req)
}

// ❌ 错误：不传递上下文或使用不一致的上下文
func (h *Handler) Create(c *gin.Context) {
    err := h.service.Create(req)
}
```

10. 测试组织：
```go
// ✅ 正确：测试文件与源文件对应
package handler

func TestUserHandler_Create(t *testing.T) {
    // 单元测试
}

// ❌ 错误：测试代码与源码混合或测试覆盖不全
func TestAll(t *testing.T) {
    // 混合测试多个功能
}
```

遵循这些规则可以使代码：
1. 更容易理解和维护
2. 更好的测试覆盖
3. 更清晰的责任边界
4. 更容易进行重构
5. 更好的扩展性

同时也避免了常见的问题如：
1. 循环依赖
2. 紧耦合
3. 难以测试
4. 难以维护
5. 代码重复



是的，还有一些重要的设计规则和最佳实践：

11. 命名规范：
```go
// ✅ 正确：清晰的命名约定
type (
    // Response 用于外部 API
    CreateUserResponse struct {
        UserID uint64 `json:"user_id"`
    }

    // DTO 用于服务层
    UserDTO struct {
        ID uint64
    }

    // DO 用于数据库层
    UserDO struct {
        ID uint64 `gorm:"column:id"`
    }
)

// ❌ 错误：命名不清晰或不一致
type (
    UserResp struct {}
    UserData struct {}
    TUser struct {}
)
```

12. 领域驱动的包组织：
```go
// ✅ 正确：按领域组织代码
project/
  ├── user/
  │   ├── handler.go
  │   ├── service.go
  │   └── repository.go
  ├── order/
  │   ├── handler.go
  │   ├── service.go
  │   └── repository.go
  └── product/
      ├── handler.go
      ├── service.go
      └── repository.go

// ❌ 错误：按技术层级组织
project/
  ├── handler/
  │   ├── user.go
  │   ├── order.go
  │   └── product.go
  └── service/
      ├── user.go
      ├── order.go
      └── product.go
```

13. 错误处理：
```go
// ✅ 正确：定义领域错误类型
package errors

type ErrorCode int

const (
    ErrNotFound ErrorCode = iota + 1
    ErrInvalidInput
    ErrUnauthorized
)

type Error struct {
    Code    ErrorCode
    Message string
    Err     error
}

// ❌ 错误：使用通用错误或字符串
if err != nil {
    return errors.New("something went wrong")
}
```

14. 中间件链管理：
```go
// ✅ 正确：中间件配置集中管理
func SetupMiddlewares(r *gin.Engine) {
    r.Use(
        middleware.Recovery(),
        middleware.Logger(),
        middleware.Trace(),
        middleware.Auth(),
    )
}

// ❌ 错误：中间件分散配置
r.Use(middleware.Logger())
// ... 其他代码
r.Use(middleware.Auth())
```

15. 配置验证：
```go
// ✅ 正确：配置验证和默认值
type Config struct {
    Port     int           `validate:"required,min=1024,max=65535"`
    Timeout  time.Duration `validate:"required,min=1s"`
    LogLevel string        `validate:"oneof=debug info warn error"`
}

func (c *Config) Validate() error {
    return validator.Struct(c)
}

// ❌ 错误：无验证的配置
type Config struct {
    Port     int
    Timeout  time.Duration
    LogLevel string
}
```

16. 日志处理：
```go
// ✅ 正确：结构化日志，带上下文信息
func (s *service) CreateUser(ctx context.Context, user *User) error {
    logger := log.WithContext(ctx).With(
        "user_id", user.ID,
        "action", "create_user",
    )
    logger.Info("creating user")

    if err := s.repo.Create(user); err != nil {
        logger.Error("failed to create user", "error", err)
        return err
    }
    return nil
}

// ❌ 错误：非结构化日志，信息不完整
log.Printf("error: %v", err)
```

17. 事务处理：
```go
// ✅ 正确：统一的事务管理
type TxManager interface {
    WithTx(ctx context.Context, fn func(ctx context.Context) error) error
}

func (s *service) CreateOrder(ctx context.Context, order *Order) error {
    return s.txManager.WithTx(ctx, func(ctx context.Context) error {
        // 在事务中执行操作
        if err := s.repo.Create(ctx, order); err != nil {
            return err
        }
        return s.eventRepo.Publish(ctx, "order_created", order)
    })
}

// ❌ 错误：手动事务管理
tx := db.Begin()
if err := tx.Create(order).Error; err != nil {
    tx.Rollback()
    return err
}
tx.Commit()
```

18. 缓存策略：
```go
// ✅ 正确：缓存抽象和策略
type Cache interface {
    Get(ctx context.Context, key string) (interface{}, error)
    Set(ctx context.Context, key string, value interface{}, ttl time.Duration) error
}

type UserService struct {
    repo  Repository
    cache Cache
}

// ❌ 错误：直接使用缓存实现
func (s *service) GetUser(id string) (*User, error) {
    key := fmt.Sprintf("user:%s", id)
    if val, err := redis.Get(key).Result(); err == nil {
        // 处理缓存
    }
}
```

19. 并发控制：
```go
// ✅ 正确：优雅的并发控制
func ProcessItems(items []Item) error {
    sem := make(chan struct{}, MaxConcurrent)
    errs := make(chan error, len(items))

    for _, item := range items {
        sem <- struct{}{} // 获取信号量
        go func(item Item) {
            defer func() { <-sem }() // 释放信号量
            if err := processItem(item); err != nil {
                errs <- err
            }
        }(item)
    }

    // 等待所有 goroutine 完成
    return errors.Join(errs...)
}

// ❌ 错误：无控制的并发
for _, item := range items {
    go processItem(item)
}
```

20. 优雅关闭：
```go
// ✅ 正确：优雅关闭服务
func main() {
    ctx, cancel := context.WithCancel(context.Background())
    defer cancel()

    go func() {
        sigCh := make(chan os.Signal, 1)
        signal.Notify(sigCh, syscall.SIGINT, syscall.SIGTERM)
        <-sigCh
        cancel()
    }()

    if err := server.Run(ctx); err != nil {
        log.Fatal(err)
    }
}

// ❌ 错误：直接退出
func main() {
    if err := server.Run(); err != nil {
        os.Exit(1)
    }
}
```

这些规则和最佳实践能帮助你：
1. 提高代码质量和可维护性
2. 减少 bug 和技术债务
3. 提高团队协作效率
4. 使系统更加健壮和可靠
5. 便于扩展和重构



这个接口定义应该放在 handler 包中。原因如下：

1. 依赖关系:
   - Handler 依赖 Service
   - 接口应该由调用方(Handler)定义，而不是实现方(Service)定义
   - 这样符合依赖倒置原则(DIP)

2. 导入循环:
   - 如果接口定义在 service 包中，会导致包循环引用的问题：
     * handler 包需要导入 service 包来使用数据结构
     * service 包需要导入 handler 包来实现接口

让我来展示正确的结构：

这样组织代码的好处是：

1. 符合依赖倒置原则：
   - 高层模块(Handler)不依赖于低层模块(Service)
   - 两者都依赖于抽象(接口)
   - 抽象由调用方定义，不依赖于具体实现

2. 避免循环依赖：
   - Handler 定义接口和数据结构
   - Service 实现接口，使用 Handler 中定义的类型
   - Repository 层不需要知道上层的存在

3. 清晰的依赖方向：
   ```
   Handler (定义接口) <- Service (实现接口) <- Repository
   ```

4. 更好的测试性：
   - 可以轻松为 Handler 创建 Service 的 mock
   - 接口和数据结构集中在一处，易于维护

5. 更容易进行修改：
   - 如果需要修改接口，只需要修改 Handler 包
   - 实现方(Service)会得到编译错误提示，确保实现完整性

是的，还有更多重要的设计规则和最佳实践：

21. 参数验证：
```go
// ✅ 正确：分层的参数验证
// handler 层：验证 API 参数格式
type CreateUserRequest struct {
    Username string `json:"username" binding:"required,min=3,max=32"`
    Email    string `json:"email" binding:"required,email"`
    Age      int    `json:"age" binding:"required,gte=0,lte=150"`
}

// service 层：验证业务规则
func (s *UserService) Create(ctx context.Context, dto *UserDTO) error {
    if err := s.validateBusinessRules(ctx, dto); err != nil {
        return fmt.Errorf("business validation failed: %w", err)
    }
    // ...
}

// ❌ 错误：验证逻辑混乱或重复
if username == "" || len(username) < 3 {
    return errors.New("invalid username")
}
```

22. 模块化配置：
```go
// ✅ 正确：模块化的配置管理
type Config struct {
    HTTP     HTTPConfig     `mapstructure:"http"`
    Database DatabaseConfig `mapstructure:"database"`
    Cache    CacheConfig    `mapstructure:"cache"`
}

type HTTPConfig struct {
    Port         int           `mapstructure:"port" validate:"required"`
    ReadTimeout  time.Duration `mapstructure:"read_timeout" validate:"required"`
    WriteTimeout time.Duration `mapstructure:"write_timeout" validate:"required"`
}

// ❌ 错误：平铺的配置结构
type Config struct {
    HTTPPort         int
    HTTPReadTimeout  time.Duration
    HTTPWriteTimeout time.Duration
    DBHost          string
    DBPort          int
    DBUser          string
    // ...
}
```

23. 资源管理：
```go
// ✅ 正确：统一的资源管理器
type ResourceManager struct {
    db    *gorm.DB
    redis *redis.Client
    es    *elasticsearch.Client
}

func NewResourceManager() *ResourceManager {
    return &ResourceManager{
        db:    initDB(),
        redis: initRedis(),
        es:    initElasticsearch(),
    }
}

func (rm *ResourceManager) Close() error {
    var errs []error
    if err := rm.db.Close(); err != nil {
        errs = append(errs, fmt.Errorf("db close error: %w", err))
    }
    if err := rm.redis.Close(); err != nil {
        errs = append(errs, fmt.Errorf("redis close error: %w", err))
    }
    return errors.Join(errs...)
}

// ❌ 错误：分散的资源管理
var (
    db    *gorm.DB
    redis *redis.Client
)
```

24. 环境配置：
```go
// ✅ 正确：环境感知的配置
type Environment string

const (
    EnvDevelopment Environment = "development"
    EnvStaging     Environment = "staging"
    EnvProduction  Environment = "production"
)

type Config struct {
    Env Environment `mapstructure:"env" validate:"required,oneof=development staging production"`
}

func (c *Config) IsDevelopment() bool { return c.Env == EnvDevelopment }
func (c *Config) IsProduction() bool  { return c.Env == EnvProduction }

// ❌ 错误：硬编码的环境判断
if os.Getenv("ENV") == "prod" {
    // ...
}
```

25. 监控指标：
```go
// ✅ 正确：结构化的监控指标
const (
    MetricRequestTotal     = "http_requests_total"
    MetricRequestDuration  = "http_request_duration_seconds"
    MetricDatabaseQueries  = "database_queries_total"
)

type Metrics interface {
    Counter(name string, labels map[string]string) float64
    Histogram(name string, value float64, labels map[string]string)
    Gauge(name string, value float64, labels map[string]string)
}

// ❌ 错误：临时或非结构化的监控
log.Printf("request took %v", time.Since(start))
```

26. API 版本控制：
```go
// ✅ 正确：显式的 API 版本控制
func SetupRoutes(r *gin.Engine) {
    v1 := r.Group("/api/v1")
    {
        users := v1.Group("/users")
        users.POST("/", handler.CreateUserV1)
    }

    v2 := r.Group("/api/v2")
    {
        users := v2.Group("/users")
        users.POST("/", handler.CreateUserV2)
    }
}

// ❌ 错误：隐式或缺少版本控制
r.POST("/api/users", handler.CreateUser)
```

27. 依赖注入容器：
```go
// ✅ 正确：使用依赖注入容器
type Container struct {
    services map[reflect.Type]interface{}
    mu       sync.RWMutex
}

func (c *Container) Register(service interface{}) {
    c.mu.Lock()
    defer c.mu.Unlock()
    c.services[reflect.TypeOf(service)] = service
}

func (c *Container) Resolve(t reflect.Type) interface{} {
    c.mu.RLock()
    defer c.mu.RUnlock()
    return c.services[t]
}

// ❌ 错误：全局变量依赖
var (
    userService    *UserService
    orderService   *OrderService
)
```

28. 数据库迁移：
```go
// ✅ 正确：版本化的数据库迁移
type Migration struct {
    Version     uint64
    Description string
    UpSQL       string
    DownSQL     string
}

var migrations = []Migration{
    {
        Version:     1,
        Description: "Create users table",
        UpSQL:       `CREATE TABLE users (...)`,
        DownSQL:     `DROP TABLE users`,
    },
    // ...
}

// ❌ 错误：手动或非版本化的迁移
func initDatabase() {
    db.Exec("CREATE TABLE IF NOT EXISTS users (...)")
}
```

29. 文档生成：
```go
// ✅ 正确：自动化的文档生成
// @Summary 创建用户
// @Description 创建新用户并返回用户ID
// @Tags users
// @Accept json
// @Produce json
// @Param user body CreateUserRequest true "用户信息"
// @Success 200 {object} CreateUserResponse
// @Router /api/v1/users [post]
func (h *UserHandler) Create(c *gin.Context) {
    // ...
}

// ❌ 错误：手动维护或缺少文档
func (h *UserHandler) Create(c *gin.Context) {
    // TODO: add documentation
}
```

30. 测试数据工厂：
```go
// ✅ 正确：使用测试数据工厂
type UserFactory struct {
    faker *faker.Faker
}

func (f *UserFactory) MakeUser(opts ...UserOption) *User {
    user := &User{
        Username: f.faker.Internet().UserName(),
        Email:    f.faker.Internet().Email(),
    }

    for _, opt := range opts {
        opt(user)
    }
    return user
}

// ❌ 错误：硬编码测试数据
user := &User{
    Username: "test_user",
    Email:    "test@example.com",
}
```

这些规则和最佳实践能帮助你：
1. 提高代码的可测试性
2. 增强系统的可观测性
3. 简化部署和运维
4. 提高开发效率
5. 减少潜在问题

建议根据项目的具体需求和团队情况，选择合适的规则来遵循。不必一次性实现所有规则，可以渐进式地改进。





是的，还有更多高级的设计规则和最佳实践：

31. 限流器实现：
```go
// ✅ 正确：可配置的限流器
type RateLimiter struct {
    tokens         chan struct{}
    refillInterval time.Duration
}

func NewRateLimiter(rate int, interval time.Duration) *RateLimiter {
    rl := &RateLimiter{
        tokens:         make(chan struct{}, rate),
        refillInterval: interval,
    }

    // 初始填充令牌
    for i := 0; i < rate; i++ {
        rl.tokens <- struct{}{}
    }

    // 定期补充令牌
    go rl.refill()
    return rl
}

// middleware 使用
func RateLimitMiddleware(rl *RateLimiter) gin.HandlerFunc {
    return func(c *gin.Context) {
        select {
        case <-rl.tokens:
            c.Next()
        default:
            c.JSON(429, gin.H{"error": "too many requests"})
            c.Abort()
        }
    }
}

// ❌ 错误：简单计数器限流
var (
    count     int
    mu        sync.Mutex
    lastReset time.Time
)
```

32. 重试策略：
```go
// ✅ 正确：可配置的重试策略
type RetryConfig struct {
    MaxRetries  int
    BaseDelay   time.Duration
    MaxDelay    time.Duration
    Multiplier  float64
    ShouldRetry func(error) bool
}

func WithRetry(ctx context.Context, fn func() error, cfg RetryConfig) error {
    var lastErr error
    for attempt := 0; attempt < cfg.MaxRetries; attempt++ {
        if err := fn(); err != nil {
            if !cfg.ShouldRetry(err) {
                return err
            }
            lastErr = err
            delay := time.Duration(float64(cfg.BaseDelay) * math.Pow(cfg.Multiplier, float64(attempt)))
            if delay > cfg.MaxDelay {
                delay = cfg.MaxDelay
            }
            select {
            case <-ctx.Done():
                return ctx.Err()
            case <-time.After(delay):
                continue
            }
        }
        return nil
    }
    return fmt.Errorf("max retries exceeded: %w", lastErr)
}

// ❌ 错误：硬编码重试逻辑
for i := 0; i < 3; i++ {
    if err := doSomething(); err == nil {
        break
    }
    time.Sleep(time.Second)
}
```

33. 工作池模式：
```go
// ✅ 正确：通用工作池实现
type Pool struct {
    tasks     chan func()
    workers   int
    wg        sync.WaitGroup
    ctx       context.Context
    cancel    context.CancelFunc
}

func NewPool(workers int) *Pool {
    ctx, cancel := context.WithCancel(context.Background())
    p := &Pool{
        tasks:   make(chan func()),
        workers: workers,
        ctx:     ctx,
        cancel:  cancel,
    }
    p.start()
    return p
}

func (p *Pool) start() {
    for i := 0; i < p.workers; i++ {
        p.wg.Add(1)
        go func() {
            defer p.wg.Done()
            for {
                select {
                case task, ok := <-p.tasks:
                    if !ok {
                        return
                    }
                    task()
                case <-p.ctx.Done():
                    return
                }
            }
        }()
    }
}

// ❌ 错误：为每个任务创建 goroutine
for _, task := range tasks {
    go process(task)
}
```

34. 断路器模式：
```go
// ✅ 正确：断路器实现
type CircuitBreaker struct {
    mu           sync.RWMutex
    failureCount int
    lastFailure  time.Time
    state        State
    threshold    int
    timeout      time.Duration
}

type State int

const (
    StateClosed State = iota
    StateHalfOpen
    StateOpen
)

func (cb *CircuitBreaker) Execute(fn func() error) error {
    if !cb.allowRequest() {
        return ErrCircuitOpen
    }

    err := fn()
    cb.recordResult(err)
    return err
}

// ❌ 错误：无保护的外部调用
response, err := http.Get(url)
```

35. 优雅降级：
```go
// ✅ 正确：降级策略
type Fallback struct {
    Primary   func() (interface{}, error)
    Secondary func() (interface{}, error)
    Cache     Cache
}

func (f *Fallback) Execute() (interface{}, error) {
    // 尝试主要实现
    result, err := f.Primary()
    if err == nil {
        return result, nil
    }

    // 尝试缓存
    if cached, err := f.Cache.Get(); err == nil {
        return cached, nil
    }

    // 使用备用实现
    return f.Secondary()
}

// ❌ 错误：无降级处理
result, err := getPrimaryData()
if err != nil {
    return err
}
```

36. 服务健康检查：
```go
// ✅ 正确：结构化的健康检查
type HealthChecker struct {
    checks map[string]HealthCheck
}

type HealthCheck func() error

func (h *HealthChecker) AddCheck(name string, check HealthCheck) {
    h.checks[name] = check
}

func (h *HealthChecker) RunChecks() map[string]string {
    results := make(map[string]string)
    for name, check := range h.checks {
        if err := check(); err != nil {
            results[name] = fmt.Sprintf("unhealthy: %v", err)
        } else {
            results[name] = "healthy"
        }
    }
    return results
}

// ❌ 错误：简单的 ping 检查
func healthCheck(w http.ResponseWriter, r *http.Request) {
    w.Write([]byte("ok"))
}
```

37. 应用指标收集：
```go
// ✅ 正确：结构化的指标收集
type Metrics struct {
    counters   map[string]*atomic.Int64
    histograms map[string]*metrics.Histogram
    mu         sync.RWMutex
}

func (m *Metrics) RecordLatency(name string, duration time.Duration) {
    m.mu.RLock()
    histogram, exists := m.histograms[name]
    m.mu.RUnlock()

    if exists {
        histogram.Observe(duration.Seconds())
    }
}

// ❌ 错误：简单日志记录
log.Printf("operation took %v", time.Since(start))
```

38. 链路追踪：
```go
// ✅ 正确：完整的链路追踪
type Tracer struct {
    spans map[string]*Span
}

type Span struct {
    TraceID    string
    SpanID     string
    ParentID   string
    Operation  string
    StartTime  time.Time
    EndTime    time.Time
    Attributes map[string]string
}

func (t *Tracer) StartSpan(ctx context.Context, op string) (*Span, context.Context) {
    parent := SpanFromContext(ctx)
    span := &Span{
        TraceID:    generateTraceID(),
        SpanID:     generateSpanID(),
        Operation:  op,
        StartTime:  time.Now(),
        Attributes: make(map[string]string),
    }
    if parent != nil {
        span.ParentID = parent.SpanID
    }
    return span, ContextWithSpan(ctx, span)
}

// ❌ 错误：仅记录开始和结束
start := time.Now()
defer func() {
    log.Printf("operation took %v", time.Since(start))
}()
```

这些高级模式可以帮助你：
1. 提高系统的可靠性
2. 增强系统的弹性
3. 改善系统的可观测性
4. 优化性能
5. 更好地处理异常情况

重要提示：
1. 这些模式应根据实际需求选择使用
2. 不要过度设计
3. 应该渐进式地引入这些模式
4. 需要考虑维护成本
5. 团队的技术能力要匹配

你还需要了解其他方面的内容吗？





是的，让我继续分享一些高级设计模式和最佳实践：

39. 缓存策略模式：
```go
// ✅ 正确：可插拔的缓存策略
type CacheStrategy interface {
    Get(ctx context.Context, key string) (interface{}, error)
    Set(ctx context.Context, key string, value interface{}, ttl time.Duration) error
    Delete(ctx context.Context, key string) error
}

// 多级缓存策略
type MultiLevelCache struct {
    l1 CacheStrategy // 本地缓存
    l2 CacheStrategy // Redis缓存
}

func (m *MultiLevelCache) Get(ctx context.Context, key string) (interface{}, error) {
    // 先查本地缓存
    if val, err := m.l1.Get(ctx, key); err == nil {
        return val, nil
    }

    // 查Redis缓存
    val, err := m.l2.Get(ctx, key)
    if err != nil {
        return nil, err
    }

    // 回填本地缓存
    go m.l1.Set(ctx, key, val, time.Minute)
    return val, nil
}

// ❌ 错误：硬编码的缓存逻辑
if val, err := localCache.Get(key); err == nil {
    return val
}
return redisCache.Get(key)
```

40. 数据库读写分离：
```go
// ✅ 正确：读写分离封装
type Database struct {
    master *gorm.DB
    slaves []*gorm.DB
    mu     sync.RWMutex
    index  uint64 // 用于轮询
}

func (db *Database) Master() *gorm.DB {
    return db.master
}

func (db *Database) Slave() *gorm.DB {
    db.mu.RLock()
    defer db.mu.RUnlock()

    if len(db.slaves) == 0 {
        return db.master
    }

    // 轮询选择从库
    index := atomic.AddUint64(&db.index, 1)
    return db.slaves[index%uint64(len(db.slaves))]
}

// 使用示例
func (r *UserRepo) Create(ctx context.Context, user *User) error {
    return r.db.Master().Create(user).Error
}

func (r *UserRepo) Find(ctx context.Context, id uint64) (*User, error) {
    var user User
    err := r.db.Slave().First(&user, id).Error
    return &user, err
}

// ❌ 错误：不区分读写的数据库操作
db.Create(user)
db.First(&user)
```

41. 消息队列封装：
```go
// ✅ 正确：抽象的消息队列接口
type MessageQueue interface {
    Publish(ctx context.Context, topic string, msg interface{}) error
    Subscribe(ctx context.Context, topic string, handler MessageHandler) error
}

type MessageHandler func(ctx context.Context, msg []byte) error

// Kafka实现
type KafkaQueue struct {
    producer sarama.SyncProducer
    consumer sarama.ConsumerGroup
}

func (k *KafkaQueue) Publish(ctx context.Context, topic string, msg interface{}) error {
    data, err := json.Marshal(msg)
    if err != nil {
        return err
    }

    _, _, err = k.producer.SendMessage(&sarama.ProducerMessage{
        Topic: topic,
        Value: sarama.ByteEncoder(data),
    })
    return err
}

// ❌ 错误：直接使用消息队列客户端
producer.SendMessage(&sarama.ProducerMessage{...})
```

42. 分布式锁：
```go
// ✅ 正确：分布式锁接口和实现
type DistributedLock interface {
    Lock(ctx context.Context) error
    Unlock(ctx context.Context) error
}

// Redis实现
type RedisLock struct {
    client  *redis.Client
    key     string
    value   string
    expires time.Duration
}

func (l *RedisLock) Lock(ctx context.Context) error {
    ok, err := l.client.SetNX(ctx, l.key, l.value, l.expires).Result()
    if err != nil {
        return err
    }
    if !ok {
        return ErrLockAcquireFailed
    }
    return nil
}

func (l *RedisLock) Unlock(ctx context.Context) error {
    script := `
        if redis.call("get", KEYS[1]) == ARGV[1] then
            return redis.call("del", KEYS[1])
        else
            return 0
        end
    `
    return l.client.Eval(ctx, script, []string{l.key}, l.value).Err()
}

// ❌ 错误：简单的互斥锁
var mu sync.Mutex
```

43. 业务规则引擎：
```go
// ✅ 正确：可配置的规则引擎
type Rule interface {
    Evaluate(ctx context.Context, facts map[string]interface{}) (bool, error)
}

type CompositeRule struct {
    rules    []Rule
    operator string // "and" or "or"
}

func (c *CompositeRule) Evaluate(ctx context.Context, facts map[string]interface{}) (bool, error) {
    switch c.operator {
    case "and":
        for _, rule := range c.rules {
            ok, err := rule.Evaluate(ctx, facts)
            if err != nil {
                return false, err
            }
            if !ok {
                return false, nil
            }
        }
        return true, nil
    case "or":
        for _, rule := range c.rules {
            ok, err := rule.Evaluate(ctx, facts)
            if err != nil {
                return false, err
            }
            if ok {
                return true, nil
            }
        }
        return false, nil
    default:
        return false, fmt.Errorf("unknown operator: %s", c.operator)
    }
}

// ❌ 错误：硬编码的业务规则
if user.Age >= 18 && user.Country == "CN" {
    // ...
}
```

44. 配置热更新：
```go
// ✅ 正确：支持热更新的配置
type DynamicConfig struct {
    mu      sync.RWMutex
    current atomic.Value
    watch   chan struct{}
}

func (c *DynamicConfig) Watch() {
    go func() {
        for {
            select {
            case <-c.watch:
                // 配置变更通知
                if err := c.reload(); err != nil {
                    log.Printf("reload config error: %v", err)
                }
            }
        }
    }()
}

func (c *DynamicConfig) reload() error {
    c.mu.Lock()
    defer c.mu.Unlock()

    // 加载新配置
    newConfig, err := loadConfig()
    if err != nil {
        return err
    }

    // 原子更新
    c.current.Store(newConfig)
    return nil
}

// ❌ 错误：静态配置
var config = loadConfig()
```

45. 权限控制：
```go
// ✅ 正确：RBAC权限系统
type Permission string

const (
    PermissionUserCreate Permission = "user:create"
    PermissionUserRead   Permission = "user:read"
    PermissionUserUpdate Permission = "user:update"
    PermissionUserDelete Permission = "user:delete"
)

type RBAC struct {
    roles       map[string][]Permission
    userRoles   map[string][]string
}

func (r *RBAC) Can(userID string, perm Permission) bool {
    roles := r.userRoles[userID]
    for _, role := range roles {
        perms := r.roles[role]
        for _, p := range perms {
            if p == perm {
                return true
            }
        }
    }
    return false
}

// 中间件使用
func RequirePermission(perm Permission) gin.HandlerFunc {
    return func(c *gin.Context) {
        userID := GetUserID(c)
        if !rbac.Can(userID, perm) {
            c.AbortWithStatus(http.StatusForbidden)
            return
        }
        c.Next()
    }
}

// ❌ 错误：简单的角色检查
if user.Role != "admin" {
    return errors.New("permission denied")
}
```

这些高级模式和最佳实践可以帮助你：
1. 实现更复杂的业务需求
2. 提高系统的可扩展性
3. 增强代码的可维护性
4. 提升系统性能
5. 更好地处理分布式场景

关键建议：
1. 根据实际需求选择合适的模式
2. 避免过度设计
3. 考虑团队的技术水平
4. 注意维护成本
5. 持续优化和改进

需要了解更多其他方面的内容吗？

是的，让我们继续探讨更多高级设计模式和实践：

46. 领域事件处理：
```go
// ✅ 正确：领域事件处理
type DomainEvent interface {
    EventName() string
    OccurredAt() time.Time
}

type EventHandler interface {
    Handle(ctx context.Context, event DomainEvent) error
}

type EventBus struct {
    handlers map[string][]EventHandler
    mu       sync.RWMutex
}

// 用户创建事件
type UserCreatedEvent struct {
    UserID    uint64
    Username  string
    CreatedAt time.Time
}

func (e UserCreatedEvent) EventName() string {
    return "user.created"
}

// 事件处理器
type EmailNotifier struct {
    emailService EmailService
}

func (n *EmailNotifier) Handle(ctx context.Context, event DomainEvent) error {
    userCreated, ok := event.(*UserCreatedEvent)
    if !ok {
        return errors.New("invalid event type")
    }
    return n.emailService.SendWelcomeEmail(userCreated.UserID)
}

// 使用示例
func (s *UserService) Create(ctx context.Context, user *User) error {
    if err := s.repo.Create(ctx, user); err != nil {
        return err
    }

    // 发布领域事件
    event := &UserCreatedEvent{
        UserID:    user.ID,
        Username:  user.Username,
        CreatedAt: time.Now(),
    }
    return s.eventBus.Publish(ctx, event)
}

// ❌ 错误：直接在服务中处理副作用
func (s *UserService) Create(ctx context.Context, user *User) error {
    if err := s.repo.Create(ctx, user); err != nil {
        return err
    }
    s.emailService.SendWelcomeEmail(user.ID) // 紧耦合
    return nil
}
```

47. 幂等性处理：
```go
// ✅ 正确：幂等性控制器
type IdempotencyKey string

type IdempotencyControl struct {
    redis *redis.Client
}

func (ic *IdempotencyControl) Process(
    ctx context.Context,
    key IdempotencyKey,
    ttl time.Duration,
    fn func() error,
) error {
    // 使用 Redis 的 SETNX 实现幂等性检查
    ok, err := ic.redis.SetNX(ctx, string(key), "processing", ttl).Result()
    if err != nil {
        return fmt.Errorf("idempotency check failed: %w", err)
    }
    if !ok {
        return ErrDuplicateRequest
    }

    // 执行业务逻辑
    if err := fn(); err != nil {
        // 业务执行失败，删除幂等键
        ic.redis.Del(ctx, string(key))
        return err
    }

    // 更新状态为已完成
    return ic.redis.Set(ctx, string(key), "completed", ttl).Err()
}

// 使用示例
func (s *PaymentService) ProcessPayment(ctx context.Context, req *PaymentRequest) error {
    key := IdempotencyKey(fmt.Sprintf("payment:%s", req.OrderID))
    return s.idempotency.Process(ctx, key, 24*time.Hour, func() error {
        return s.processPaymentLogic(ctx, req)
    })
}

// ❌ 错误：无幂等性控制
func (s *PaymentService) ProcessPayment(ctx context.Context, req *PaymentRequest) error {
    return s.processPaymentLogic(ctx, req)
}
```

48. 异步任务处理：
```go
// ✅ 正确：异步任务系统
type Task struct {
    ID        string
    Type      string
    Payload   json.RawMessage
    Status    TaskStatus
    Result    json.RawMessage
    CreatedAt time.Time
    UpdatedAt time.Time
}

type TaskProcessor interface {
    Process(ctx context.Context, task *Task) error
}

type TaskQueue struct {
    processors map[string]TaskProcessor
    repo       TaskRepository
}

func (q *TaskQueue) Submit(ctx context.Context, taskType string, payload interface{}) (*Task, error) {
    data, err := json.Marshal(payload)
    if err != nil {
        return nil, err
    }

    task := &Task{
        ID:        uuid.New().String(),
        Type:      taskType,
        Payload:   data,
        Status:    TaskStatusPending,
        CreatedAt: time.Now(),
    }

    if err := q.repo.Save(ctx, task); err != nil {
        return nil, err
    }

    // 异步处理任务
    go q.process(context.Background(), task)
    return task, nil
}

// 使用示例
type EmailTask struct {
    To      string `json:"to"`
    Subject string `json:"subject"`
    Body    string `json:"body"`
}

func (s *EmailService) SendAsync(ctx context.Context, to, subject, body string) (*Task, error) {
    task := &EmailTask{
        To:      to,
        Subject: subject,
        Body:    body,
    }
    return s.taskQueue.Submit(ctx, "email", task)
}

// ❌ 错误：直接在 goroutine 中处理
go sendEmail(to, subject, body)
```

49. 审计日志：
```go
// ✅ 正确：审计日志系统
type AuditLog struct {
    ID        uint64
    UserID    uint64
    Action    string
    Resource  string
    ResourceID string
    Changes   map[string]interface{}
    IP        string
    UserAgent string
    CreatedAt time.Time
}

type AuditLogger struct {
    repo AuditLogRepository
}

func (l *AuditLogger) Log(ctx context.Context, event *AuditEvent) error {
    log := &AuditLog{
        UserID:    GetUserID(ctx),
        Action:    event.Action,
        Resource:  event.Resource,
        ResourceID: event.ResourceID,
        Changes:   event.Changes,
        IP:        GetClientIP(ctx),
        UserAgent: GetUserAgent(ctx),
        CreatedAt: time.Now(),
    }
    return l.repo.Create(ctx, log)
}

// 中间件使用
func AuditMiddleware(logger *AuditLogger) gin.HandlerFunc {
    return func(c *gin.Context) {
        // 记录请求前的状态
        // ...

        c.Next()

        // 记录请求后的状态变化
        event := &AuditEvent{
            Action:    c.Request.Method,
            Resource:  c.Request.URL.Path,
            Changes:   getChanges(c),
        }
        logger.Log(c, event)
    }
}

// ❌ 错误：简单的日志记录
log.Printf("user %d modified resource %s", userID, resourceID)
```

50. API 版本控制和兼容性：
```go
// ✅ 正确：API 版本控制
type APIVersion string

const (
    APIVersionV1 APIVersion = "v1"
    APIVersionV2 APIVersion = "v2"
)

// 请求结构体版本控制
type CreateUserRequestV1 struct {
    Username string `json:"username"`
    Password string `json:"password"`
}

type CreateUserRequestV2 struct {
    Username  string `json:"username"`
    Password  string `json:"password"`
    PhoneNumber string `json:"phone_number"`  // V2新增字段
}

// 服务层版本控制
type UserService interface {
    CreateUserV1(ctx context.Context, req *CreateUserRequestV1) error
    CreateUserV2(ctx context.Context, req *CreateUserRequestV2) error
}

// 路由版本控制
func SetupRoutes(r *gin.Engine) {
    v1 := r.Group("/api/v1")
    {
        v1.POST("/users", handler.CreateUserV1)
    }

    v2 := r.Group("/api/v2")
    {
        v2.POST("/users", handler.CreateUserV2)
    }
}

// ❌ 错误：不兼容的API变更
type CreateUserRequest struct {
    Username string    `json:"username"`
    Password string    `json:"password"`
    // 直接修改已发布的API结构
    PhoneNumber string `json:"phone_number"`
}
```

这些设计模式和最佳实践适用于：
1. 大型复杂系统
2. 微服务架构
3. 高可用要求的系统
4. 需要严格审计的系统
5. 需要良好扩展性的系统

要点提示：
1. 根据实际需求选择合适的模式
2. 在简单系统中避免过度设计
3. 考虑团队的技术能力和维护成本
4. 保持代码的可测试性
5. 注重文档和注释的维护

需要了解更多其他方面的内容吗？





这些最佳实践和设计模式来源于多个领域，我来整理一下来源和推荐阅读：

1. Go 语言最佳实践来源：

```markdown
书籍：
1. 《Go Programming Language》 - Alan A. A. Donovan, Brian W. Kernighan
   - Go 语言权威指南，基础语法和最佳实践

2. 《100 Go Mistakes and How to Avoid Them》 - Teiva Harsanyi
   - 详细介绍 Go 常见错误和避免方法

3. 《Concurrency in Go》 - Katherine Cox-Buday
   - Go 并发编程最佳实践

在线资源：
1. Go 官方文档和博客：https://golang.org/doc/
2. Uber Go 风格指南：https://github.com/uber-go/guide
3. Go Code Review Comments：https://github.com/golang/go/wiki/CodeReviewComments
4. effective_go：https://golang.org/doc/effective_go
```

2. 架构设计参考：

```markdown
书籍：
1. 《Clean Architecture》 - Robert C. Martin
   - 架构设计原则和最佳实践

2. 《Designing Data-Intensive Applications》 - Martin Kleppmann
   - 分布式系统设计圣经

3. 《Domain-Driven Design》 - Eric Evans
   - 领域驱动设计

4. 《Building Microservices》 - Sam Newman
   - 微服务架构设计

在线资源：
1. Microsoft Azure Architecture Center：https://docs.microsoft.com/azure/architecture/
2. AWS Architecture Center：https://aws.amazon.com/architecture/
3. System Design Primer：https://github.com/donnemartin/system-design-primer
```

3. 设计模式：

```markdown
书籍：
1. 《Design Patterns》 - Gang of Four
   - 经典设计模式

2. 《Go Design Patterns》 - Mario Castro Contreras
   - Go 语言设计模式实现

3. 《Cloud Native Go》 - Matthew A. Titmus
   - 云原生 Go 应用设计模式

在线资源：
1. Go Patterns：https://github.com/tmrts/go-patterns
2. Cloud Native Patterns：https://www.cnpatterns.org/
```

4. 数据库和性能优化：

```markdown
书籍：
1. 《High Performance MySQL》 - Baron Schwartz
   - MySQL 性能优化指南

2. 《Database Internals》 - Alex Petrov
   - 数据库内部原理

在线资源：
1. GORM 文档：https://gorm.io/docs/
2. MySQL 官方文档：https://dev.mysql.com/doc/
```

5. 微服务和分布式系统：

```markdown
书籍：
1. 《Microservices Patterns》 - Chris Richardson
   - 微服务设计模式

2. 《Site Reliability Engineering》 - Google
   - Google SRE 实践

在线资源：
1. Go Micro：https://go-micro.dev/
2. Go Kit：https://gokit.io/
```

6. 安全最佳实践：

```markdown
书籍：
1. 《Web Application Security》 - Andrew Hoffman
   - Web 应用安全指南

在线资源：
1. OWASP：https://owasp.org/
2. Go Security Cheat Sheet：https://github.com/OWASP/CheatSheetSeries
```

7. 测试和质量保证：

```markdown
书籍：
1. 《Test-Driven Development with Go》 - Adelina Simion
   - Go TDD 实践

在线资源：
1. Go Testing：https://golang.org/pkg/testing/
2. GoMock：https://github.com/golang/mock
```

8. 持续学习资源：

```markdown
1. Go Weekly：https://golangweekly.com/
2. Go Time Podcast：https://changelog.com/gotime
3. Go Forum：https://forum.golangbridge.org/
4. Reddit r/golang：https://www.reddit.com/r/golang/
```

实践建议：

1. 循序渐进：
   - 从基础开始，逐步掌握高级概念
   - 在实际项目中应用所学知识

2. 社区参与：
   - 关注 Go 语言社区动态
   - 参与开源项目
   - 分享经验和学习心得

3. 实践为主：
   - 多写代码，多做项目
   - 复现和实现书中的示例
   - 根据实际需求选择合适的模式

4. 持续更新：
   - 关注新版本特性
   - 学习新的最佳实践
   - 保持对技术的热情

这些资源和建议可以帮助你：
1. 系统地学习 Go 开发
2. 提高代码质量
3. 掌握先进的架构设计
4. 解决实际问题
5. 持续进步

你对哪些方面特别感兴趣？我可以给出更具体的学习建议。









# Go 后端开发学习路线图

## 1. 基础架构
### 1.1 分层架构
- Handler (API) 层
  - 参数验证
  - 错误处理
  - 响应封装
  - 路由管理
  - API 文档 (Swagger)

- Service (业务) 层
  - 业务逻辑
  - 事务管理
  - 领域模型
  - 数据转换
  - 业务规则验证

- Repository (数据) 层
  - 数据访问
  - ORM 使用
  - SQL 优化
  - 缓存管理
  - 数据模型

### 1.2 依赖管理
- 依赖注入原则
- 接口定义位置
- 依赖方向控制
- 循环依赖处理
- 模块化设计

### 1.3 配置管理
- 环境配置
- 配置分离
- 配置验证
- 敏感信息保护
- 热更新支持

## 2. 性能优化
### 2.1 并发控制
- Goroutine 池
- 工作池模式
- 并发限制
- 竞态条件处理
- 上下文管理

### 2.2 数据库优化
- 连接池管理
- 读写分离
- 分库分表
- 索引优化
- 慢查询处理

### 2.3 缓存策略
- 多级缓存
- 缓存一致性
- 缓存穿透
- 缓存雪崩
- 缓存更新

## 3. 可靠性保障
### 3.1 错误处理
- 错误类型定义
- 错误包装
- 错误传播
- 错误恢复
- 错误监控

### 3.2 重试机制
- 退避策略
- 超时控制
- 熔断器模式
- 降级策略
- 限流控制

### 3.3 事务管理
- 本地事务
- 分布式事务
- 补偿事务
- 事务隔离级别
- 死锁处理

## 4. 安全性保障
### 4.1 认证授权
- JWT 实现
- OAuth2 集成
- RBAC 权限
- 会话管理
- 权限校验

### 4.2 数据安全
- 加密解密
- 敏感数据处理
- SQL 注入防护
- XSS 防护
- CSRF 防护

### 4.3 访问控制
- 限流
- 黑白名单
- IP 控制
- 请求频率控制
- 资源隔离

## 5. 可观测性
### 5.1 日志管理
- 结构化日志
- 日志分级
- 日志轮转
- 审计日志
- 日志收集

### 5.2 监控指标
- 性能指标
- 业务指标
- 系统指标
- 告警策略
- 指标可视化

### 5.3 链路追踪
- 请求追踪
- 性能分析
- 调用链路
- 异常定位
- 性能瓶颈

## 6. 最佳实践
### 6.1 代码规范
- 项目结构
- 命名规范
- 注释规范
- 代码格式
- 最佳实践

### 6.2 设计模式
- 创建型模式
- 结构型模式
- 行为型模式
- DDD 实践
- 微服务模式

### 6.3 测试规范
- 单元测试
- 集成测试
- 性能测试
- 压力测试
- 测试覆盖率

## 7. 工程化实践
### 7.1 CI/CD
- 自动构建
- 自动测试
- 自动部署
- 版本控制
- 环境管理

### 7.2 文档管理
- API 文档
- 架构文档
- 运维文档
- 变更记录
- 使用指南

### 7.3 质量保障
- 代码审查
- 静态分析
- 性能分析
- 安全扫描
- 质量监控

## 8. 中间件使用
### 8.1 消息队列
- Kafka
- RabbitMQ
- Redis Pub/Sub
- 消息幂等性
- 顺序保证

### 8.2 缓存中间件
- Redis
- Memcached
- 本地缓存
- 分布式缓存
- 缓存策略

### 8.3 搜索引擎
- Elasticsearch
- 全文搜索
- 数据同步
- 搜索优化
- 聚合分析

## 9. 微服务架构
### 9.1 服务治理
- 服务注册
- 服务发现
- 负载均衡
- 配置中心
- 服务网关

### 9.2 容器化
- Docker
- Kubernetes
- 服务编排
- 资源管理
- 容器监控

### 9.3 高可用设计
- 服务容错
- 灾难恢复
- 数据备份
- 多活部署
- 自动扩缩容

## 10. 架构进阶
### 10.1 领域驱动设计
- 领域模型
- 限界上下文
- 聚合根
- 领域事件
- CQRS

### 10.2 分布式系统
- CAP 理论
- 一致性算法
- 分布式锁
- 分布式事务
- 分布式缓存

### 10.3 性能调优
- 系统调优
- 网络调优
- 数据库调优
- 应用调优
- 代码调优











让我总结一下在 Go 和 Rust 中常见的接口设计和依赖管理最佳实践：

Go 语言接口设计原则：

1. 接口定义位置：
```go
// 接口应该由调用方定义，而不是实现方
caller/   -> 定义接口
service/  -> 实现接口
```

2. 小接口原则：
```go
// 好的设计
type Reader interface {
    Read(p []byte) (n int, err error)
}

type Writer interface {
    Write(p []byte) (n int, err error)
}

// 需要时可以组合
type ReadWriter interface {
    Reader
    Writer
}
```

3. 面向抽象编程：
```go
// Handler 依赖接口而不是具体实现
type Handler struct {
    service ServiceInterface  // 好
    // service *ConcreteService  // 不好
}
```

Rust 中的类似原则：

1. 特征(Trait)定义位置：
```rust
// 在调用方 crate 中定义特征
mod caller {
    pub trait ImageService {
        fn upload(&self, image: Image) -> Result<(), Error>;
    }
}

// 在实现方 crate 中实现特征
mod service {
    use caller::ImageService;

    struct MyImageService;

    impl ImageService for MyImageService {
        fn upload(&self, image: Image) -> Result<(), Error> {
            // 实现
        }
    }
}
```

2. 特征边界和泛型：
```rust
// 使用特征边界而不是具体类型
struct Handler<S: ImageService> {
    service: S,
}

// 或者使用 impl Trait
fn new_handler(service: impl ImageService) -> Handler<impl ImageService> {
    Handler { service }
}
```

3. 面向特征编程：
```rust
// 好的设计
pub trait Repository {
    fn save(&self, data: &[u8]) -> Result<(), Error>;
}

// 实现可以放在单独的模块
pub struct FileRepository;
impl Repository for FileRepository {
    // 实现
}

// 使用 Box<dyn Trait> 实现运行时多态
struct Service {
    repo: Box<dyn Repository>,
}
```

4. 依赖注入模式：
```rust
// 使用构建器模式
pub struct ServiceBuilder<R> {
    repository: R,
}

impl<R: Repository> ServiceBuilder<R> {
    pub fn new(repository: R) -> Self {
        Self { repository }
    }

    pub fn build(self) -> Service<R> {
        Service {
            repository: self.repository,
        }
    }
}
```

5. 错误处理：
```rust
// 定义域特定错误
#[derive(Debug, thiserror::Error)]
pub enum ServiceError {
    #[error("database error: {0}")]
    Database(#[from] DbError),
    #[error("validation error: {0}")]
    Validation(String),
}

// 实现时使用 ? 运算符传播错误
impl ImageService for MyService {
    fn process(&self, data: &[u8]) -> Result<(), ServiceError> {
        let validated = validate_data(data)?;
        self.repository.save(validated)?;
        Ok(())
    }
}
```

6. 模块化和可见性：
```rust
// 在 lib.rs 中定义公共 API
pub mod api {
    pub trait Service {
        // 公共接口
    }
}

// 内部实现保持私有
mod internal {
    use super::api::Service;

    pub(crate) struct ServiceImpl;

    impl Service for ServiceImpl {
        // 实现
    }
}
```

共同的设计原则：

1. 依赖倒置：
   - 高层模块不应该依赖低层模块
   - 都应该依赖于抽象

2. 单一职责：
   - 每个接口/特征应该只负责一个功能领域
   - 避免大而全的接口/特征

3. 接口隔离：
   - 客户端不应该依赖它不需要的接口
   - 使用小而精确的接口/特征

4. 显式依赖：
   - 通过构造函数/builder注入依赖
   - 避免全局状态和隐式依赖

这些原则能帮助我们创建：
- 松耦合的系统
- 易于测试的代码
- 可维护的项目结构
- 清晰的依赖关系
