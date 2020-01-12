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
using System.IO;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Reflection;
using RestSharp;
using NUnit.Framework;

using IO.Swagger.Client;
using IO.Swagger.Api;
using IO.Swagger.Model;

namespace IO.Swagger.Test
{
    /// <summary>
    ///  Class for testing AccountsApi
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by Swagger Codegen.
    /// Please update the test case below to test the API endpoint.
    /// </remarks>
    [TestFixture]
    public class AccountsApiTests
    {
        private AccountsApi instance;

        /// <summary>
        /// Setup before each unit test
        /// </summary>
        [SetUp]
        public void Init()
        {
            instance = new AccountsApi();
        }

        /// <summary>
        /// Clean up after each unit test
        /// </summary>
        [TearDown]
        public void Cleanup()
        {

        }

        /// <summary>
        /// Test an instance of AccountsApi
        /// </summary>
        [Test]
        public void InstanceTest()
        {
            // TODO uncomment below to test 'IsInstanceOfType' AccountsApi
            //Assert.IsInstanceOfType(typeof(AccountsApi), instance, "instance is a AccountsApi");
        }

        /// <summary>
        /// Test CreateAccount
        /// </summary>
        [Test]
        public void CreateAccountTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //RequestAccount body = null;
            //long? customerId = null;
            //var response = instance.CreateAccount(body, customerId);
            //Assert.IsInstanceOf<Account> (response, "response is Account");
        }
        /// <summary>
        /// Test DeleteAccount
        /// </summary>
        [Test]
        public void DeleteAccountTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //long? accountId = null;
            //instance.DeleteAccount(accountId);
            
        }
        /// <summary>
        /// Test GetAccount
        /// </summary>
        [Test]
        public void GetAccountTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //long? accountId = null;
            //var response = instance.GetAccount(accountId);
            //Assert.IsInstanceOf<Account> (response, "response is Account");
        }
        /// <summary>
        /// Test ListAccounts
        /// </summary>
        [Test]
        public void ListAccountsTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //long? customerId = null;
            //var response = instance.ListAccounts(customerId);
            //Assert.IsInstanceOf<List<Account>> (response, "response is List<Account>");
        }
    }

}
