# IO.Swagger.Api.AccountsApi

All URIs are relative to *https://virtserver.swaggerhub.com/AndreiBarbuOz/ui-bank/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateAccount**](AccountsApi.md#createaccount) | **POST** /customer/{customerId}/accounts | Creates an account
[**DeleteAccount**](AccountsApi.md#deleteaccount) | **DELETE** /accounts/{accountId} | Deletes an account
[**GetAccount**](AccountsApi.md#getaccount) | **GET** /accounts/{accountId} | Get details for an account
[**ListAccounts**](AccountsApi.md#listaccounts) | **GET** /customer/{customerId}/accounts | List all customer accounts

<a name="createaccount"></a>
# **CreateAccount**
> Account CreateAccount (RequestAccount body, long? customerId)

Creates an account

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class CreateAccountExample
    {
        public void main()
        {

            var apiInstance = new AccountsApi();
            var body = new RequestAccount(); // RequestAccount | List of user object
            var customerId = 789;  // long? | Owner of the accounts

            try
            {
                // Creates an account
                Account result = apiInstance.CreateAccount(body, customerId);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling AccountsApi.CreateAccount: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestAccount**](RequestAccount.md)| List of user object | 
 **customerId** | **long?**| Owner of the accounts | 

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="deleteaccount"></a>
# **DeleteAccount**
> void DeleteAccount (long? accountId)

Deletes an account

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class DeleteAccountExample
    {
        public void main()
        {

            var apiInstance = new AccountsApi();
            var accountId = 789;  // long? | Id of account to delete

            try
            {
                // Deletes an account
                apiInstance.DeleteAccount(accountId);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling AccountsApi.DeleteAccount: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **long?**| Id of account to delete | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="getaccount"></a>
# **GetAccount**
> Account GetAccount (long? accountId)

Get details for an account

Returns a single account, based on accountId

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class GetAccountExample
    {
        public void main()
        {

            var apiInstance = new AccountsApi();
            var accountId = 789;  // long? | Id of account

            try
            {
                // Get details for an account
                Account result = apiInstance.GetAccount(accountId);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling AccountsApi.GetAccount: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **long?**| Id of account | 

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="listaccounts"></a>
# **ListAccounts**
> List<Account> ListAccounts (long? customerId)

List all customer accounts

Return a list of all accounts belonging to a customer

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ListAccountsExample
    {
        public void main()
        {

            var apiInstance = new AccountsApi();
            var customerId = 789;  // long? | Owner of the accounts

            try
            {
                // List all customer accounts
                List&lt;Account&gt; result = apiInstance.ListAccounts(customerId);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling AccountsApi.ListAccounts: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customerId** | **long?**| Owner of the accounts | 

### Return type

[**List<Account>**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
