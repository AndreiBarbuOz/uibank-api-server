# IO.Swagger.Api.UsersApi

All URIs are relative to *https://virtserver.swaggerhub.com/AndreiBarbuOz/ui-bank/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddUser**](UsersApi.md#adduser) | **POST** /users | Add a new admin user
[**GetUser**](UsersApi.md#getuser) | **GET** /users/{userId} | Returns user information

<a name="adduser"></a>
# **AddUser**
> User AddUser (RequestUser body)

Add a new admin user

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class AddUserExample
    {
        public void main()
        {

            var apiInstance = new UsersApi();
            var body = new RequestUser(); // RequestUser | User data to create

            try
            {
                // Add a new admin user
                User result = apiInstance.AddUser(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling UsersApi.AddUser: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestUser**](RequestUser.md)| User data to create | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="getuser"></a>
# **GetUser**
> User GetUser (long? userId)

Returns user information

Returns information about one user

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class GetUserExample
    {
        public void main()
        {

            var apiInstance = new UsersApi();
            var userId = 789;  // long? | Id of user

            try
            {
                // Returns user information
                User result = apiInstance.GetUser(userId);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling UsersApi.GetUser: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | **long?**| Id of user | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
