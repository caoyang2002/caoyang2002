+++
date = '2024-04-12T09:31:37+08:00'
draft = true
title = 'JWT 解析'
toc = true
+++

![JWT]()

[原文一](https://zhuanlan.zhihu.com/p/86937325)

[原文二](https://blog.csdn.net/weixin_39779004/article/details/110801387)

[视频](https://b23.tv/3f7Yrct)

# 一、什么是 JWT

JSON Web Token (JWT)是一个开放标准(RFC 7519)，它定义了一种紧凑的、自包含的方式，用于作为JSON对象在各方之间安全地传输信息。该信息可以被验证和信任，因为它是数字签名的。





# 二、设计目标

不需要服务器端存储状态，安全地传递非敏感信息

![JWT认证方案讲解-阿里云开发者社区](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/OIP-C-20240424140338352.jpeg)

# 三、 JSON Web Token 的结构是什么样的

JSON Web Token由三部分组成，例如`dafdsafdwfefeqwad.oijhdaffweqtgfdhfdws.dhshfsghhhhhwfsdke`

简化：`xxxxx.yyyyy.zzzzz`

可以看到它们之间用圆点(.)连接。

而这三部分分别是：

- Header 头部
- Payload 载荷
- Signature 签名



## 1. Header

由两部分组成：

- token的类型（“JWT”）
- 签名算法名称（比如：HMAC SHA256或者RSA等等）

例如：

```python
{
    'alg': "HS256",
    'typ': "JWT"
}
```

然后，用 Base64 对这个 JSON 编码就得到JWT的第一部分



## 2. Payload

> 标准声明：就是该开放标准预先定义的一些字段
>
> 公共声明：是自定义的声明，用于特定应用程序中共享信息
>
> 私有声明：用于在同意双方之间共享信息，通常不会被 JWT 规范定义，而是由应用程序自行定义和使用

它包含声明（要求）。声明是关于实体(通常是用户)和其他数据的声明。声明有三种类型: registered, public 和 private。

- Registered claims : 这里有一组预定义的声明，它们不是强制的，但是推荐。比如：iss (issuer), exp (expiration time), sub (subject), aud (audience)等。
- Public claims : 可以随意定义。
- Private claims : 用于在同意使用它们的各方之间共享信息，并且不是注册的或公开的声明。 下面是一个例子：

```python
{
    "sub": '1234567890',
    "name": 'john',
    "admin":true
}
```

对payload进行Base64编码就得到JWT的第二部分

注意，不要在JWT的payload或header中放置敏感信息，除非它们是加密的。

## 3. Signature

> 为了得到签名部分，你必须有编码过的header、编码过的payload、一个秘钥，签名算法是header中指定的那个，然对它们签名即可。

例如：

> `HMACSHA256(secret, base64UrlEncode(header) + "." + base64UrlEncode(payload))`
>
> - secret 保存在服务端，用来进行 JWT 的签发和验证，所以在任何时候都不应该泄漏
>
> - JWT 的签发生成也在服务端
>
> - HMACSHA256 是一种对称加密算法
>
>     > 对称加密算法：用一个密钥加密解密的算法
>     >
>     > 非对称加密算法：SSH key（用公钥加密的密文智能用私钥解密，用私钥签发的签名只能用公钥来验证）
>     >
>     > ![（68）对称加密和非对称加密的区别 - 走看看](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/63d0f703918fa0ec16f456372c9759ee3d6ddbdc.jpg)

签名是用于验证消息在传递过程中有没有被更改，并且，对于使用私钥签名的token，它还可以验证JWT的发送方是否为它所称的发送方。

看一张官网的图就明白了：

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/v2-2d4a2985706ff9610ad1466b66ba09ad_1440w.webp)





# JWT 是如何工作的

在认证的时候，当用户用他们的凭证成功登录以后，一个JSON Web Token将会被返回。此后，token就是用户凭证了，你必须非常小心以防止出现安全问题。一般而言，你保存令牌的时候不应该超过你所需要它的时间。

无论何时用户想要访问受保护的路由或者资源的时候，用户代理（通常是浏览器）都应该带上JWT，典型的，通常放在Authorization header中，用Bearer schema。

header应该看起来是这样的：

> Authorization: Bearer

服务器上的受保护的路由将会检查Authorization header中的JWT是否有效，如果有效，则用户可以访问受保护的资源。如果JWT包含足够多的必需的数据，那么就可以减少对某些操作的数据库查询的需要，尽管可能并不总是如此。

如果token是在授权头（Authorization header）中发送的，那么跨源资源共享(CORS)将不会成为问题，因为它不使用cookie。

# 三、场景

下列场景中使用JSON Web Token是很有用的：

- Authorization (认证、授权) : 这是使用JWT的最常见场景。一旦用户登录，后续每个请求都将包含JWT，允许用户访问该令牌允许的路由、服务和资源。单点登录是现在广泛使用的JWT的一个特性，因为它的开销很小，并且可以轻松地跨域使用。
- Information Exchange (信息交换) : 对于安全的在各方之间传输信息而言，JSON Web Tokens无疑是一种很好的方式。因为JWT可以被签名，例如，用公钥/私钥对，你可以确定发送人就是它们所说的那个人。另外，由于签名是使用头和有效负载计算的，您还可以验证内容没有被篡改。

- 基于Token的身份认证

- 基于服务器的身份认证



## 1. 基于 Token 的身份认证

在讨论基于Token的身份认证是如何工作的以及它的好处之前，我们先来看一下以前我们是怎么做的：

> HTTP 协议是无状态的，也就是说，如果我们已经认证了一个用户，那么他下一次请求的时候，服务器不知道我是谁，我们必须再次认证

传统的做法是将已经认证过的用户信息存储在服务器上，比如Session。用户下次请求的时候带着Session ID，然后服务器以此检查用户是否认证过。

这种基于服务器的身份认证方式存在一些问题：

- Sessions : 每次用户认证通过以后，服务器需要创建一条记录保存用户信息，通常是在内存中，随着认证通过的用户越来越多，服务器的在这里的开销就会越来越大。
- Scalability : 由于Session是在内存中的，这就带来一些扩展性的问题。
- CORS : 当我们想要扩展我们的应用，让我们的数据被多个移动设备使用时，我们必须考虑跨资源共享问题。当使用AJAX调用从另一个域名下获取资源时，我们可能会遇到禁止请求的问题。
- CSRF : 用户很容易受到CSRF攻击。

5.2. JWT与Session的差异 相同点是，它们都是存储用户信息；然而，Session是在服务器端的，而JWT是在客户端的。

Session方式存储用户信息的最大问题在于要占用大量服务器内存，增加服务器的开销。

而JWT方式将用户状态分散到了客户端中，可以明显减轻服务端的内存压力。

Session的状态是存储在服务器端，客户端只有session id；而Token的状态是存储在客户端。



![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/v2-b7eeaf69feb5cbbadea7e0c73056da7a_1440w.webp)



基于Token的身份认证是如何工作的 基于Token的身份认证是无状态的，服务器或者Session中不会存储任何用户信息。

没有会话信息意味着应用程序可以根据需要扩展和添加更多的机器，而不必担心用户登录的位置。

虽然这一实现可能会有所不同，但其主要流程如下：

-用户携带用户名和密码请求访问 -服务器校验用户凭据 -应用提供一个token给客户端 -客户端存储token，并且在随后的每一次请求中都带着它 -服务器校验token并返回数据

注意：

-每一次请求都需要token -Token应该放在请求header中 -我们还需要将服务器设置为接受来自所有域的请求，用Access-Control-Allow-Origin: *

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/v2-7789057d5744891fdf3366d7887ab6e8_1440w.webp)



5.4. 用Token的好处 - 无状态和可扩展性：Tokens存储在客户端。完全无状态，可扩展。我们的负载均衡器可以将用户传递到任意服务器，因为在任何地方都没有状态或会话信息。 - 安全：Token不是Cookie。（The token, not a cookie.）每次请求的时候Token都会被发送。而且，由于没有Cookie被发送，还有助于防止CSRF攻击。即使在你的实现中将token存储到客户端的Cookie中，这个Cookie也只是一种存储机制，而非身份认证机制。没有基于会话的信息可以操作，因为我们没有会话!

还有一点，token在一段时间以后会过期，这个时候用户需要重新登录。这有助于我们保持安全。还有一个概念叫token撤销，它允许我们根据相同的授权许可使特定的token甚至一组token无效。

5.5. JWT与OAuth的区别 -OAuth2是一种授权框架 ，JWT是一种认证协议 -无论使用哪种方式切记用HTTPS来保证数据的安全性 -OAuth2用在使用第三方账号登录的情况(比如使用weibo, qq, github登录某个app)，而JWT是用在前后端分离, 需要简单的对后台API进行保护时使用。

## 2. 基于服务器的身份认证

![image-20240424133914569](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/image-20240424133914569.png)

![image-20240424134647596](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/image-20240424134647596.png)

> 注意：
>
> 1. 服务器不能真正退出登录
> 2. 用户信息修改后不能及时同步
> 3. Token 泄漏后没有有效的手段将 Token 置为无效

用户通过用户名和密码登录后，系统签发一个 JWT 给客户端，这个 Token 保存了一些用户的基本信息，以及权限相关的信息，后续用户请求的时候带上这个 Token ，服务器就知道当前访问的用户是谁、有哪些权限，而不用查询数据库去3获取用户的基本信息以及权限。




## 3. 密码重置和电子邮件验证

服务器会生成包含用户信息的 JWT，并组成一个链接发到用户的邮箱，用户点击该链接后就可以重置密码或完成电子邮件验证（不是必须用 JWT）

## 4. 单点登录

![JWT单点登录 看这一篇就够了！_c# jwt单点登录-CSDN博客](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0VzcGVjaWFsbHlfQWxsZW4=,size_16,color_FFFFFF,t_70.png)

#![JWT实现SSO单点登录的流程步骤 - 开发技术 - 亿速云](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/1533.png)


# JWS （Json Web Signature）

只对内容做签名，确保其不被篡改，但是其内容本身并没有被加密。（最常见的实现 JWT 实现方式）

它的头部和载荷都是没有加密的，所以它的目的并不是想隐藏数据，而是防止数据被篡改，这点是通过第三方签名来实现的

# JWE（Json Web Encryption）

会对内容本身加密，相对更安全，但是成本也会更高。





# 对比sesion

![jwt单点登录_手把手教你，使用JWT实现单点登录-CSDN博客](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/9266406fb490f417a835b8b338913c9d.jpeg)



# 对比 Token

![img](https://mielgo-markdown.oss-cn-chengdu.aliyuncs.com/024c30b33de98d05dc4521ba7cdd9bee.jpeg)



---

jwt就是个生成token（用户令牌）的一个规范。session id 也是一种用户令牌。
就是这个令牌里面带的用户信息，表名是哪个用户的令牌。
jwt里存的用户id，也可以存redis里。也可以不存。传统的session id 是在服务器存储服务中。
过期时间可以各种设计，可以在服务端存储，也可以带到jwt里。如果是带到jwt传里的，那某个用户的jwt串只能同时有一个生效，还是只要在没过过期时间内的都有效，这个要怎么控制。
有各种设计，本质上jwt就是个把用户id安全的传给客户端，客户端安全的传给服务端。



每个用户一个sha256哈希的密码，某个用户密码被破了，就改掉这个密码。 jwt和传统session(包括说的token)，唯一区别就是 服务端保存不保存这个token。然后是，jwt带的身份标识到了服务端后，需要获取权限。session的那个id 也可以存到redis里。redis key就是session的id，value就是鉴权信息。jwt的话，想要增加速度，鉴权信息得查出来后 也可以把鉴权的信息存储到redis里，那么问题来了，到底会不会节省服务器的内存？ 估计只会省掉存储身份id这个空间。
jwt还有个好处，就是服务器，redis炸了，session id的话就会丢失，jwt的话 还在。
