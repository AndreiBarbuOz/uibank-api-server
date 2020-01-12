# IO.Swagger.Api.CustomersApi

All URIs are relative to *https://virtserver.swaggerhub.com/AndreiBarbuOz/ui-bank/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddCustomer**](CustomersApi.md#addcustomer) | **POST** /customers | Add a new customer
[**DeleteCustomer**](CustomersApi.md#deletecustomer) | **DELETE** /customers/{customerId} | Delete a single customer
[**GetCustomerDetails**](CustomersApi.md#getcustomerdetails) | **GET** /customers/{customerId} | Get customer details
[**SearchCustomer**](CustomersApi.md#searchcustomer) | **GET** /customers/search | Search for Customers
[**UpdateCustomer**](CustomersApi.md#updatecustomer) | **PUT** /customers/{customerId} | Update an existing customer

<a name="addcustomer"></a>
# **AddCustomer**
> Customer AddCustomer (RequestCustomer body)

Add a new customer

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class AddCustomerExample
    {
        public void main()
        {

            var apiInstance = new CustomersApi();
            var body = new RequestCustomer(); // RequestCustomer | Pet object that needs to be added to the store

            try
            {
                // Add a new customer
                Customer result = apiInstance.AddCustomer(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling CustomersApi.AddCustomer: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestCustomer**](RequestCustomer.md)| Pet object that needs to be added to the store | 

### Return type

[**Customer**](Customer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="deletecustomer"></a>
# **DeleteCustomer**
> void DeleteCustomer (long? customerId)

Delete a single customer

Delete customer, based on customerId

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class DeleteCustomerExample
    {
        public void main()
        {

            var apiInstance = new CustomersApi();
            var customerId = 789;  // long? | Customer to be deleted

            try
            {
                // Delete a single customer
                apiInstance.DeleteCustomer(customerId);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling CustomersApi.DeleteCustomer: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customerId** | **long?**| Customer to be deleted | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="getcustomerdetails"></a>
# **GetCustomerDetails**
> Customer GetCustomerDetails (long? customerId)

Get customer details

Retrieve the details of a customer

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class GetCustomerDetailsExample
    {
        public void main()
        {

            var apiInstance = new CustomersApi();
            var customerId = 789;  // long? | The customerId

            try
            {
                // Get customer details
                Customer result = apiInstance.GetCustomerDetails(customerId);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling CustomersApi.GetCustomerDetails: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customerId** | **long?**| The customerId | 

### Return type

[**Customer**](Customer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="searchcustomer"></a>
# **SearchCustomer**
> List<Customer> SearchCustomer (string firstName = null, string lastName = null)

Search for Customers

Search for customers using multiple search criteria

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class SearchCustomerExample
    {
        public void main()
        {

            var apiInstance = new CustomersApi();
            var firstName = firstName_example;  // string | First name to filter by (optional) 
            var lastName = lastName_example;  // string | Last name to filter by (optional) 

            try
            {
                // Search for Customers
                List&lt;Customer&gt; result = apiInstance.SearchCustomer(firstName, lastName);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling CustomersApi.SearchCustomer: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firstName** | **string**| First name to filter by | [optional] 
 **lastName** | **string**| Last name to filter by | [optional] 

### Return type

[**List<Customer>**](Customer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="updatecustomer"></a>
# **UpdateCustomer**
> void UpdateCustomer (RequestCustomer body, long? customerId)

Update an existing customer

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class UpdateCustomerExample
    {
        public void main()
        {

            var apiInstance = new CustomersApi();
            var body = new RequestCustomer(); // RequestCustomer | Pet object that needs to be added to the store
            var customerId = 789;  // long? | The customerId

            try
            {
                // Update an existing customer
                apiInstance.UpdateCustomer(body, customerId);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling CustomersApi.UpdateCustomer: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestCustomer**](RequestCustomer.md)| Pet object that needs to be added to the store | 
 **customerId** | **long?**| The customerId | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
