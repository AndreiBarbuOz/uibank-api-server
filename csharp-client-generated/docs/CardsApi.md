# IO.Swagger.Api.CardsApi

All URIs are relative to *https://virtserver.swaggerhub.com/AndreiBarbuOz/ui-bank/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddBankCard**](CardsApi.md#addbankcard) | **POST** /accounts/{accountId}/cards | Add a new bank card for an account
[**GetCard**](CardsApi.md#getcard) | **GET** /cards/{cardId} | Return all bank cards for an account
[**ListBankCards**](CardsApi.md#listbankcards) | **GET** /accounts/{accountId}/cards | Return all bank cards for an account

<a name="addbankcard"></a>
# **AddBankCard**
> BankCard AddBankCard (BankCard body, long? accountId)

Add a new bank card for an account

Add a new card for the specified account

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class AddBankCardExample
    {
        public void main()
        {

            var apiInstance = new CardsApi();
            var body = new BankCard(); // BankCard | Bank card details
            var accountId = 789;  // long? | Id of account

            try
            {
                // Add a new bank card for an account
                BankCard result = apiInstance.AddBankCard(body, accountId);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling CardsApi.AddBankCard: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BankCard**](BankCard.md)| Bank card details | 
 **accountId** | **long?**| Id of account | 

### Return type

[**BankCard**](BankCard.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="getcard"></a>
# **GetCard**
> BankCard GetCard (long? cardId)

Return all bank cards for an account

Return all cards for the specified account

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class GetCardExample
    {
        public void main()
        {

            var apiInstance = new CardsApi();
            var cardId = 789;  // long? | Id of the card

            try
            {
                // Return all bank cards for an account
                BankCard result = apiInstance.GetCard(cardId);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling CardsApi.GetCard: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cardId** | **long?**| Id of the card | 

### Return type

[**BankCard**](BankCard.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="listbankcards"></a>
# **ListBankCards**
> List<BankCard> ListBankCards (long? accountId)

Return all bank cards for an account

Return all cards for the specified account

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class ListBankCardsExample
    {
        public void main()
        {

            var apiInstance = new CardsApi();
            var accountId = 789;  // long? | Id of account

            try
            {
                // Return all bank cards for an account
                List&lt;BankCard&gt; result = apiInstance.ListBankCards(accountId);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling CardsApi.ListBankCards: " + e.Message );
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

[**List<BankCard>**](BankCard.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
