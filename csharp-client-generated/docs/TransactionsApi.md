# IO.Swagger.Api.TransactionsApi

All URIs are relative to *https://virtserver.swaggerhub.com/AndreiBarbuOz/ui-bank/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddTransaction**](TransactionsApi.md#addtransaction) | **POST** /accounts/{accountId}/transactions | Returns one transaction data
[**GetTransaction**](TransactionsApi.md#gettransaction) | **GET** /transactions/{transactionId} | Returns one transaction data
[**ListTransactions**](TransactionsApi.md#listtransactions) | **GET** /accounts/{accountId}/transactions | Return all transactions for an account

<a name="addtransaction"></a>
# **AddTransaction**
> void AddTransaction (long? accountId, RequestTransaction body = null)

Returns one transaction data

Returns one transaction data

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class AddTransactionExample
    {
        public void main()
        {

            var apiInstance = new TransactionsApi();
            var accountId = 789;  // long? | Id of account
            var body = new RequestTransaction(); // RequestTransaction |  (optional) 

            try
            {
                // Returns one transaction data
                apiInstance.AddTransaction(accountId, body);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling TransactionsApi.AddTransaction: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **long?**| Id of account | 
 **body** | [**RequestTransaction**](RequestTransaction.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="gettransaction"></a>
# **GetTransaction**
> Transaction GetTransaction (long? transactionId)

Returns one transaction data

Returns one transaction data

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class GetTransactionExample
    {
        public void main()
        {

            var apiInstance = new TransactionsApi();
            var transactionId = 789;  // long? | Id of transaction

            try
            {
                // Returns one transaction data
                Transaction result = apiInstance.GetTransaction(transactionId);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling TransactionsApi.GetTransaction: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactionId** | **long?**| Id of transaction | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="listtransactions"></a>
# **ListTransactions**
> List<Transaction> ListTransactions (long? accountId)

Return all transactions for an account

List all transactions belonging to an account

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ListTransactionsExample
    {
        public void main()
        {

            var apiInstance = new TransactionsApi();
            var accountId = 789;  // long? | Id of account

            try
            {
                // Return all transactions for an account
                List&lt;Transaction&gt; result = apiInstance.ListTransactions(accountId);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling TransactionsApi.ListTransactions: " + e.Message );
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

[**List<Transaction>**](Transaction.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
