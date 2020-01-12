# IO.Swagger.Api.AuthApi

All URIs are relative to *https://virtserver.swaggerhub.com/AndreiBarbuOz/ui-bank/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**Auth**](AuthApi.md#auth) | **POST** /auth | Authenticate endpoint

<a name="auth"></a>
# **Auth**
> Auth Auth (RequestAuth body)

Authenticate endpoint

Return a bearer token to authenticate and authorize subsequent calls for resources

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class AuthExample
    {
        public void main()
        {

            var apiInstance = new AuthApi();
            var body = new RequestAuth(); // RequestAuth | Request body to perform authentication

            try
            {
                // Authenticate endpoint
                Auth result = apiInstance.Auth(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling AuthApi.Auth: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestAuth**](RequestAuth.md)| Request body to perform authentication | 

### Return type

[**Auth**](Auth.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
