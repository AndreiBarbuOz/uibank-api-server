/* 
 * UiBank
 *
 * Sample banking API used for demoing UiPath Testing Automation. 
 *
 * OpenAPI spec version: 1.0.0
 * Contact: andrei.barbu@uipath.com
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using RestSharp;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace IO.Swagger.Api
{
    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
        public interface ITransactionsApi : IApiAccessor
    {
        #region Synchronous Operations
        /// <summary>
        /// Returns one transaction data
        /// </summary>
        /// <remarks>
        /// Returns one transaction data
        /// </remarks>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="accountId">Id of account</param>
        /// <param name="body"> (optional)</param>
        /// <returns></returns>
        void AddTransaction (long? accountId, RequestTransaction body = null);

        /// <summary>
        /// Returns one transaction data
        /// </summary>
        /// <remarks>
        /// Returns one transaction data
        /// </remarks>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="accountId">Id of account</param>
        /// <param name="body"> (optional)</param>
        /// <returns>ApiResponse of Object(void)</returns>
        ApiResponse<Object> AddTransactionWithHttpInfo (long? accountId, RequestTransaction body = null);
        /// <summary>
        /// Returns one transaction data
        /// </summary>
        /// <remarks>
        /// Returns one transaction data
        /// </remarks>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="transactionId">Id of transaction</param>
        /// <returns>Transaction</returns>
        Transaction GetTransaction (long? transactionId);

        /// <summary>
        /// Returns one transaction data
        /// </summary>
        /// <remarks>
        /// Returns one transaction data
        /// </remarks>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="transactionId">Id of transaction</param>
        /// <returns>ApiResponse of Transaction</returns>
        ApiResponse<Transaction> GetTransactionWithHttpInfo (long? transactionId);
        /// <summary>
        /// Return all transactions for an account
        /// </summary>
        /// <remarks>
        /// List all transactions belonging to an account
        /// </remarks>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="accountId">Id of account</param>
        /// <returns>List&lt;Transaction&gt;</returns>
        List<Transaction> ListTransactions (long? accountId);

        /// <summary>
        /// Return all transactions for an account
        /// </summary>
        /// <remarks>
        /// List all transactions belonging to an account
        /// </remarks>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="accountId">Id of account</param>
        /// <returns>ApiResponse of List&lt;Transaction&gt;</returns>
        ApiResponse<List<Transaction>> ListTransactionsWithHttpInfo (long? accountId);
        #endregion Synchronous Operations
        #region Asynchronous Operations
        /// <summary>
        /// Returns one transaction data
        /// </summary>
        /// <remarks>
        /// Returns one transaction data
        /// </remarks>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="accountId">Id of account</param>
        /// <param name="body"> (optional)</param>
        /// <returns>Task of void</returns>
        System.Threading.Tasks.Task AddTransactionAsync (long? accountId, RequestTransaction body = null);

        /// <summary>
        /// Returns one transaction data
        /// </summary>
        /// <remarks>
        /// Returns one transaction data
        /// </remarks>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="accountId">Id of account</param>
        /// <param name="body"> (optional)</param>
        /// <returns>Task of ApiResponse</returns>
        System.Threading.Tasks.Task<ApiResponse<Object>> AddTransactionAsyncWithHttpInfo (long? accountId, RequestTransaction body = null);
        /// <summary>
        /// Returns one transaction data
        /// </summary>
        /// <remarks>
        /// Returns one transaction data
        /// </remarks>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="transactionId">Id of transaction</param>
        /// <returns>Task of Transaction</returns>
        System.Threading.Tasks.Task<Transaction> GetTransactionAsync (long? transactionId);

        /// <summary>
        /// Returns one transaction data
        /// </summary>
        /// <remarks>
        /// Returns one transaction data
        /// </remarks>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="transactionId">Id of transaction</param>
        /// <returns>Task of ApiResponse (Transaction)</returns>
        System.Threading.Tasks.Task<ApiResponse<Transaction>> GetTransactionAsyncWithHttpInfo (long? transactionId);
        /// <summary>
        /// Return all transactions for an account
        /// </summary>
        /// <remarks>
        /// List all transactions belonging to an account
        /// </remarks>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="accountId">Id of account</param>
        /// <returns>Task of List&lt;Transaction&gt;</returns>
        System.Threading.Tasks.Task<List<Transaction>> ListTransactionsAsync (long? accountId);

        /// <summary>
        /// Return all transactions for an account
        /// </summary>
        /// <remarks>
        /// List all transactions belonging to an account
        /// </remarks>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="accountId">Id of account</param>
        /// <returns>Task of ApiResponse (List&lt;Transaction&gt;)</returns>
        System.Threading.Tasks.Task<ApiResponse<List<Transaction>>> ListTransactionsAsyncWithHttpInfo (long? accountId);
        #endregion Asynchronous Operations
    }

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
        public partial class TransactionsApi : ITransactionsApi
    {
        private IO.Swagger.Client.ExceptionFactory _exceptionFactory = (name, response) => null;

        /// <summary>
        /// Initializes a new instance of the <see cref="TransactionsApi"/> class.
        /// </summary>
        /// <returns></returns>
        public TransactionsApi(String basePath)
        {
            this.Configuration = new IO.Swagger.Client.Configuration { BasePath = basePath };

            ExceptionFactory = IO.Swagger.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="TransactionsApi"/> class
        /// </summary>
        /// <returns></returns>
        public TransactionsApi()
        {
            this.Configuration = IO.Swagger.Client.Configuration.Default;

            ExceptionFactory = IO.Swagger.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="TransactionsApi"/> class
        /// using Configuration object
        /// </summary>
        /// <param name="configuration">An instance of Configuration</param>
        /// <returns></returns>
        public TransactionsApi(IO.Swagger.Client.Configuration configuration = null)
        {
            if (configuration == null) // use the default one in Configuration
                this.Configuration = IO.Swagger.Client.Configuration.Default;
            else
                this.Configuration = configuration;

            ExceptionFactory = IO.Swagger.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// Gets the base path of the API client.
        /// </summary>
        /// <value>The base path</value>
        public String GetBasePath()
        {
            return this.Configuration.ApiClient.RestClient.BaseUrl.ToString();
        }

        /// <summary>
        /// Sets the base path of the API client.
        /// </summary>
        /// <value>The base path</value>
        [Obsolete("SetBasePath is deprecated, please do 'Configuration.ApiClient = new ApiClient(\"http://new-path\")' instead.")]
        public void SetBasePath(String basePath)
        {
            // do nothing
        }

        /// <summary>
        /// Gets or sets the configuration object
        /// </summary>
        /// <value>An instance of the Configuration</value>
        public IO.Swagger.Client.Configuration Configuration {get; set;}

        /// <summary>
        /// Provides a factory method hook for the creation of exceptions.
        /// </summary>
        public IO.Swagger.Client.ExceptionFactory ExceptionFactory
        {
            get
            {
                if (_exceptionFactory != null && _exceptionFactory.GetInvocationList().Length > 1)
                {
                    throw new InvalidOperationException("Multicast delegate for ExceptionFactory is unsupported.");
                }
                return _exceptionFactory;
            }
            set { _exceptionFactory = value; }
        }

        /// <summary>
        /// Gets the default header.
        /// </summary>
        /// <returns>Dictionary of HTTP header</returns>
        [Obsolete("DefaultHeader is deprecated, please use Configuration.DefaultHeader instead.")]
        public IDictionary<String, String> DefaultHeader()
        {
            return new ReadOnlyDictionary<string, string>(this.Configuration.DefaultHeader);
        }

        /// <summary>
        /// Add default header.
        /// </summary>
        /// <param name="key">Header field name.</param>
        /// <param name="value">Header field value.</param>
        /// <returns></returns>
        [Obsolete("AddDefaultHeader is deprecated, please use Configuration.AddDefaultHeader instead.")]
        public void AddDefaultHeader(string key, string value)
        {
            this.Configuration.AddDefaultHeader(key, value);
        }

        /// <summary>
        /// Returns one transaction data Returns one transaction data
        /// </summary>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="accountId">Id of account</param>
        /// <param name="body"> (optional)</param>
        /// <returns></returns>
        public void AddTransaction (long? accountId, RequestTransaction body = null)
        {
             AddTransactionWithHttpInfo(accountId, body);
        }

        /// <summary>
        /// Returns one transaction data Returns one transaction data
        /// </summary>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="accountId">Id of account</param>
        /// <param name="body"> (optional)</param>
        /// <returns>ApiResponse of Object(void)</returns>
        public ApiResponse<Object> AddTransactionWithHttpInfo (long? accountId, RequestTransaction body = null)
        {
            // verify the required parameter 'accountId' is set
            if (accountId == null)
                throw new ApiException(400, "Missing required parameter 'accountId' when calling TransactionsApi->AddTransaction");

            var localVarPath = "/accounts/{accountId}/transactions";
            var localVarPathParams = new Dictionary<String, String>();
            var localVarQueryParams = new List<KeyValuePair<String, String>>();
            var localVarHeaderParams = new Dictionary<String, String>(this.Configuration.DefaultHeader);
            var localVarFormParams = new Dictionary<String, String>();
            var localVarFileParams = new Dictionary<String, FileParameter>();
            Object localVarPostBody = null;

            // to determine the Content-Type header
            String[] localVarHttpContentTypes = new String[] {
                "application/json"
            };
            String localVarHttpContentType = this.Configuration.ApiClient.SelectHeaderContentType(localVarHttpContentTypes);

            // to determine the Accept header
            String[] localVarHttpHeaderAccepts = new String[] {
            };
            String localVarHttpHeaderAccept = this.Configuration.ApiClient.SelectHeaderAccept(localVarHttpHeaderAccepts);
            if (localVarHttpHeaderAccept != null)
                localVarHeaderParams.Add("Accept", localVarHttpHeaderAccept);

            if (accountId != null) localVarPathParams.Add("accountId", this.Configuration.ApiClient.ParameterToString(accountId)); // path parameter
            if (body != null && body.GetType() != typeof(byte[]))
            {
                localVarPostBody = this.Configuration.ApiClient.Serialize(body); // http body (model) parameter
            }
            else
            {
                localVarPostBody = body; // byte array
            }
            // authentication (bearerAuth) required

            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) this.Configuration.ApiClient.CallApi(localVarPath,
                Method.POST, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("AddTransaction", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<Object>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                null);
        }

        /// <summary>
        /// Returns one transaction data Returns one transaction data
        /// </summary>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="accountId">Id of account</param>
        /// <param name="body"> (optional)</param>
        /// <returns>Task of void</returns>
        public async System.Threading.Tasks.Task AddTransactionAsync (long? accountId, RequestTransaction body = null)
        {
             await AddTransactionAsyncWithHttpInfo(accountId, body);

        }

        /// <summary>
        /// Returns one transaction data Returns one transaction data
        /// </summary>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="accountId">Id of account</param>
        /// <param name="body"> (optional)</param>
        /// <returns>Task of ApiResponse</returns>
        public async System.Threading.Tasks.Task<ApiResponse<Object>> AddTransactionAsyncWithHttpInfo (long? accountId, RequestTransaction body = null)
        {
            // verify the required parameter 'accountId' is set
            if (accountId == null)
                throw new ApiException(400, "Missing required parameter 'accountId' when calling TransactionsApi->AddTransaction");

            var localVarPath = "/accounts/{accountId}/transactions";
            var localVarPathParams = new Dictionary<String, String>();
            var localVarQueryParams = new List<KeyValuePair<String, String>>();
            var localVarHeaderParams = new Dictionary<String, String>(this.Configuration.DefaultHeader);
            var localVarFormParams = new Dictionary<String, String>();
            var localVarFileParams = new Dictionary<String, FileParameter>();
            Object localVarPostBody = null;

            // to determine the Content-Type header
            String[] localVarHttpContentTypes = new String[] {
                "application/json"
            };
            String localVarHttpContentType = this.Configuration.ApiClient.SelectHeaderContentType(localVarHttpContentTypes);

            // to determine the Accept header
            String[] localVarHttpHeaderAccepts = new String[] {
            };
            String localVarHttpHeaderAccept = this.Configuration.ApiClient.SelectHeaderAccept(localVarHttpHeaderAccepts);
            if (localVarHttpHeaderAccept != null)
                localVarHeaderParams.Add("Accept", localVarHttpHeaderAccept);

            if (accountId != null) localVarPathParams.Add("accountId", this.Configuration.ApiClient.ParameterToString(accountId)); // path parameter
            if (body != null && body.GetType() != typeof(byte[]))
            {
                localVarPostBody = this.Configuration.ApiClient.Serialize(body); // http body (model) parameter
            }
            else
            {
                localVarPostBody = body; // byte array
            }
            // authentication (bearerAuth) required

            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) await this.Configuration.ApiClient.CallApiAsync(localVarPath,
                Method.POST, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("AddTransaction", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<Object>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                null);
        }

        /// <summary>
        /// Returns one transaction data Returns one transaction data
        /// </summary>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="transactionId">Id of transaction</param>
        /// <returns>Transaction</returns>
        public Transaction GetTransaction (long? transactionId)
        {
             ApiResponse<Transaction> localVarResponse = GetTransactionWithHttpInfo(transactionId);
             return localVarResponse.Data;
        }

        /// <summary>
        /// Returns one transaction data Returns one transaction data
        /// </summary>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="transactionId">Id of transaction</param>
        /// <returns>ApiResponse of Transaction</returns>
        public ApiResponse< Transaction > GetTransactionWithHttpInfo (long? transactionId)
        {
            // verify the required parameter 'transactionId' is set
            if (transactionId == null)
                throw new ApiException(400, "Missing required parameter 'transactionId' when calling TransactionsApi->GetTransaction");

            var localVarPath = "/transactions/{transactionId}";
            var localVarPathParams = new Dictionary<String, String>();
            var localVarQueryParams = new List<KeyValuePair<String, String>>();
            var localVarHeaderParams = new Dictionary<String, String>(this.Configuration.DefaultHeader);
            var localVarFormParams = new Dictionary<String, String>();
            var localVarFileParams = new Dictionary<String, FileParameter>();
            Object localVarPostBody = null;

            // to determine the Content-Type header
            String[] localVarHttpContentTypes = new String[] {
            };
            String localVarHttpContentType = this.Configuration.ApiClient.SelectHeaderContentType(localVarHttpContentTypes);

            // to determine the Accept header
            String[] localVarHttpHeaderAccepts = new String[] {
                "application/json"
            };
            String localVarHttpHeaderAccept = this.Configuration.ApiClient.SelectHeaderAccept(localVarHttpHeaderAccepts);
            if (localVarHttpHeaderAccept != null)
                localVarHeaderParams.Add("Accept", localVarHttpHeaderAccept);

            if (transactionId != null) localVarPathParams.Add("transactionId", this.Configuration.ApiClient.ParameterToString(transactionId)); // path parameter
            // authentication (bearerAuth) required

            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) this.Configuration.ApiClient.CallApi(localVarPath,
                Method.GET, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("GetTransaction", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<Transaction>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (Transaction) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(Transaction)));
        }

        /// <summary>
        /// Returns one transaction data Returns one transaction data
        /// </summary>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="transactionId">Id of transaction</param>
        /// <returns>Task of Transaction</returns>
        public async System.Threading.Tasks.Task<Transaction> GetTransactionAsync (long? transactionId)
        {
             ApiResponse<Transaction> localVarResponse = await GetTransactionAsyncWithHttpInfo(transactionId);
             return localVarResponse.Data;

        }

        /// <summary>
        /// Returns one transaction data Returns one transaction data
        /// </summary>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="transactionId">Id of transaction</param>
        /// <returns>Task of ApiResponse (Transaction)</returns>
        public async System.Threading.Tasks.Task<ApiResponse<Transaction>> GetTransactionAsyncWithHttpInfo (long? transactionId)
        {
            // verify the required parameter 'transactionId' is set
            if (transactionId == null)
                throw new ApiException(400, "Missing required parameter 'transactionId' when calling TransactionsApi->GetTransaction");

            var localVarPath = "/transactions/{transactionId}";
            var localVarPathParams = new Dictionary<String, String>();
            var localVarQueryParams = new List<KeyValuePair<String, String>>();
            var localVarHeaderParams = new Dictionary<String, String>(this.Configuration.DefaultHeader);
            var localVarFormParams = new Dictionary<String, String>();
            var localVarFileParams = new Dictionary<String, FileParameter>();
            Object localVarPostBody = null;

            // to determine the Content-Type header
            String[] localVarHttpContentTypes = new String[] {
            };
            String localVarHttpContentType = this.Configuration.ApiClient.SelectHeaderContentType(localVarHttpContentTypes);

            // to determine the Accept header
            String[] localVarHttpHeaderAccepts = new String[] {
                "application/json"
            };
            String localVarHttpHeaderAccept = this.Configuration.ApiClient.SelectHeaderAccept(localVarHttpHeaderAccepts);
            if (localVarHttpHeaderAccept != null)
                localVarHeaderParams.Add("Accept", localVarHttpHeaderAccept);

            if (transactionId != null) localVarPathParams.Add("transactionId", this.Configuration.ApiClient.ParameterToString(transactionId)); // path parameter
            // authentication (bearerAuth) required

            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) await this.Configuration.ApiClient.CallApiAsync(localVarPath,
                Method.GET, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("GetTransaction", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<Transaction>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (Transaction) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(Transaction)));
        }

        /// <summary>
        /// Return all transactions for an account List all transactions belonging to an account
        /// </summary>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="accountId">Id of account</param>
        /// <returns>List&lt;Transaction&gt;</returns>
        public List<Transaction> ListTransactions (long? accountId)
        {
             ApiResponse<List<Transaction>> localVarResponse = ListTransactionsWithHttpInfo(accountId);
             return localVarResponse.Data;
        }

        /// <summary>
        /// Return all transactions for an account List all transactions belonging to an account
        /// </summary>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="accountId">Id of account</param>
        /// <returns>ApiResponse of List&lt;Transaction&gt;</returns>
        public ApiResponse< List<Transaction> > ListTransactionsWithHttpInfo (long? accountId)
        {
            // verify the required parameter 'accountId' is set
            if (accountId == null)
                throw new ApiException(400, "Missing required parameter 'accountId' when calling TransactionsApi->ListTransactions");

            var localVarPath = "/accounts/{accountId}/transactions";
            var localVarPathParams = new Dictionary<String, String>();
            var localVarQueryParams = new List<KeyValuePair<String, String>>();
            var localVarHeaderParams = new Dictionary<String, String>(this.Configuration.DefaultHeader);
            var localVarFormParams = new Dictionary<String, String>();
            var localVarFileParams = new Dictionary<String, FileParameter>();
            Object localVarPostBody = null;

            // to determine the Content-Type header
            String[] localVarHttpContentTypes = new String[] {
            };
            String localVarHttpContentType = this.Configuration.ApiClient.SelectHeaderContentType(localVarHttpContentTypes);

            // to determine the Accept header
            String[] localVarHttpHeaderAccepts = new String[] {
                "application/json"
            };
            String localVarHttpHeaderAccept = this.Configuration.ApiClient.SelectHeaderAccept(localVarHttpHeaderAccepts);
            if (localVarHttpHeaderAccept != null)
                localVarHeaderParams.Add("Accept", localVarHttpHeaderAccept);

            if (accountId != null) localVarPathParams.Add("accountId", this.Configuration.ApiClient.ParameterToString(accountId)); // path parameter
            // authentication (bearerAuth) required

            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) this.Configuration.ApiClient.CallApi(localVarPath,
                Method.GET, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("ListTransactions", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<List<Transaction>>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (List<Transaction>) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(List<Transaction>)));
        }

        /// <summary>
        /// Return all transactions for an account List all transactions belonging to an account
        /// </summary>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="accountId">Id of account</param>
        /// <returns>Task of List&lt;Transaction&gt;</returns>
        public async System.Threading.Tasks.Task<List<Transaction>> ListTransactionsAsync (long? accountId)
        {
             ApiResponse<List<Transaction>> localVarResponse = await ListTransactionsAsyncWithHttpInfo(accountId);
             return localVarResponse.Data;

        }

        /// <summary>
        /// Return all transactions for an account List all transactions belonging to an account
        /// </summary>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="accountId">Id of account</param>
        /// <returns>Task of ApiResponse (List&lt;Transaction&gt;)</returns>
        public async System.Threading.Tasks.Task<ApiResponse<List<Transaction>>> ListTransactionsAsyncWithHttpInfo (long? accountId)
        {
            // verify the required parameter 'accountId' is set
            if (accountId == null)
                throw new ApiException(400, "Missing required parameter 'accountId' when calling TransactionsApi->ListTransactions");

            var localVarPath = "/accounts/{accountId}/transactions";
            var localVarPathParams = new Dictionary<String, String>();
            var localVarQueryParams = new List<KeyValuePair<String, String>>();
            var localVarHeaderParams = new Dictionary<String, String>(this.Configuration.DefaultHeader);
            var localVarFormParams = new Dictionary<String, String>();
            var localVarFileParams = new Dictionary<String, FileParameter>();
            Object localVarPostBody = null;

            // to determine the Content-Type header
            String[] localVarHttpContentTypes = new String[] {
            };
            String localVarHttpContentType = this.Configuration.ApiClient.SelectHeaderContentType(localVarHttpContentTypes);

            // to determine the Accept header
            String[] localVarHttpHeaderAccepts = new String[] {
                "application/json"
            };
            String localVarHttpHeaderAccept = this.Configuration.ApiClient.SelectHeaderAccept(localVarHttpHeaderAccepts);
            if (localVarHttpHeaderAccept != null)
                localVarHeaderParams.Add("Accept", localVarHttpHeaderAccept);

            if (accountId != null) localVarPathParams.Add("accountId", this.Configuration.ApiClient.ParameterToString(accountId)); // path parameter
            // authentication (bearerAuth) required

            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) await this.Configuration.ApiClient.CallApiAsync(localVarPath,
                Method.GET, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("ListTransactions", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<List<Transaction>>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (List<Transaction>) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(List<Transaction>)));
        }

    }
}
