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
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using SwaggerDateConverter = IO.Swagger.Client.SwaggerDateConverter;

namespace IO.Swagger.Model
{
    /// <summary>
    /// Transaction
    /// </summary>
    [DataContract]
        public partial class Transaction :  IEquatable<Transaction>, IValidatableObject
    {
        /// <summary>
        /// Transaction type
        /// </summary>
        /// <value>Transaction type</value>
        [JsonConverter(typeof(StringEnumConverter))]
                public enum TransactionTypeEnum
        {
            /// <summary>
            /// Enum Debit for value: debit
            /// </summary>
            [EnumMember(Value = "debit")]
            Debit = 0,
            /// <summary>
            /// Enum Credit for value: credit
            /// </summary>
            [EnumMember(Value = "credit")]
            Credit = 1        }
        /// <summary>
        /// Transaction type
        /// </summary>
        /// <value>Transaction type</value>
        [DataMember(Name="transaction_type", EmitDefaultValue=false)]
        public TransactionTypeEnum TransactionType { get; set; }
        /// <summary>
        /// If transaction is under dispute
        /// </summary>
        /// <value>If transaction is under dispute</value>
        [JsonConverter(typeof(StringEnumConverter))]
                public enum DisputeEnum
        {
            /// <summary>
            /// Enum No for value: no
            /// </summary>
            [EnumMember(Value = "no")]
            No = 0,
            /// <summary>
            /// Enum Reported for value: reported
            /// </summary>
            [EnumMember(Value = "reported")]
            Reported = 1,
            /// <summary>
            /// Enum Underinvestigation for value: under investigation
            /// </summary>
            [EnumMember(Value = "under investigation")]
            Underinvestigation = 2        }
        /// <summary>
        /// If transaction is under dispute
        /// </summary>
        /// <value>If transaction is under dispute</value>
        [DataMember(Name="dispute", EmitDefaultValue=false)]
        public DisputeEnum? Dispute { get; set; }
        /// <summary>
        /// Initializes a new instance of the <see cref="Transaction" /> class.
        /// </summary>
        /// <param name="id">id.</param>
        /// <param name="dateTime">dateTime (required).</param>
        /// <param name="amount">amount (required).</param>
        /// <param name="transactionType">Transaction type (required).</param>
        /// <param name="reference">reference (required).</param>
        /// <param name="description">description (required).</param>
        /// <param name="balance">balance (required).</param>
        /// <param name="dispute">If transaction is under dispute.</param>
        /// <param name="selfUrl">selfUrl (required).</param>
        /// <param name="accountUrl">accountUrl (required).</param>
        public Transaction(long? id = default(long?), DateTime? dateTime = default(DateTime?), float? amount = default(float?), TransactionTypeEnum transactionType = default(TransactionTypeEnum), string reference = default(string), string description = default(string), string balance = default(string), DisputeEnum? dispute = default(DisputeEnum?), string selfUrl = default(string), string accountUrl = default(string))
        {
            // to ensure "dateTime" is required (not null)
            if (dateTime == null)
            {
                throw new InvalidDataException("dateTime is a required property for Transaction and cannot be null");
            }
            else
            {
                this.DateTime = dateTime;
            }
            // to ensure "amount" is required (not null)
            if (amount == null)
            {
                throw new InvalidDataException("amount is a required property for Transaction and cannot be null");
            }
            else
            {
                this.Amount = amount;
            }
            // to ensure "transactionType" is required (not null)
            if (transactionType == null)
            {
                throw new InvalidDataException("transactionType is a required property for Transaction and cannot be null");
            }
            else
            {
                this.TransactionType = transactionType;
            }
            // to ensure "reference" is required (not null)
            if (reference == null)
            {
                throw new InvalidDataException("reference is a required property for Transaction and cannot be null");
            }
            else
            {
                this.Reference = reference;
            }
            // to ensure "description" is required (not null)
            if (description == null)
            {
                throw new InvalidDataException("description is a required property for Transaction and cannot be null");
            }
            else
            {
                this.Description = description;
            }
            // to ensure "balance" is required (not null)
            if (balance == null)
            {
                throw new InvalidDataException("balance is a required property for Transaction and cannot be null");
            }
            else
            {
                this.Balance = balance;
            }
            // to ensure "selfUrl" is required (not null)
            if (selfUrl == null)
            {
                throw new InvalidDataException("selfUrl is a required property for Transaction and cannot be null");
            }
            else
            {
                this.SelfUrl = selfUrl;
            }
            // to ensure "accountUrl" is required (not null)
            if (accountUrl == null)
            {
                throw new InvalidDataException("accountUrl is a required property for Transaction and cannot be null");
            }
            else
            {
                this.AccountUrl = accountUrl;
            }
            this.Id = id;
            this.Dispute = dispute;
        }
        
        /// <summary>
        /// Gets or Sets Id
        /// </summary>
        [DataMember(Name="id", EmitDefaultValue=false)]
        public long? Id { get; set; }

        /// <summary>
        /// Gets or Sets DateTime
        /// </summary>
        [DataMember(Name="date_time", EmitDefaultValue=false)]
        public DateTime? DateTime { get; set; }

        /// <summary>
        /// Gets or Sets Amount
        /// </summary>
        [DataMember(Name="amount", EmitDefaultValue=false)]
        public float? Amount { get; set; }


        /// <summary>
        /// Gets or Sets Reference
        /// </summary>
        [DataMember(Name="reference", EmitDefaultValue=false)]
        public string Reference { get; set; }

        /// <summary>
        /// Gets or Sets Description
        /// </summary>
        [DataMember(Name="description", EmitDefaultValue=false)]
        public string Description { get; set; }

        /// <summary>
        /// Gets or Sets Balance
        /// </summary>
        [DataMember(Name="balance", EmitDefaultValue=false)]
        public string Balance { get; set; }


        /// <summary>
        /// Gets or Sets SelfUrl
        /// </summary>
        [DataMember(Name="self_url", EmitDefaultValue=false)]
        public string SelfUrl { get; set; }

        /// <summary>
        /// Gets or Sets AccountUrl
        /// </summary>
        [DataMember(Name="account_url", EmitDefaultValue=false)]
        public string AccountUrl { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class Transaction {\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  DateTime: ").Append(DateTime).Append("\n");
            sb.Append("  Amount: ").Append(Amount).Append("\n");
            sb.Append("  TransactionType: ").Append(TransactionType).Append("\n");
            sb.Append("  Reference: ").Append(Reference).Append("\n");
            sb.Append("  Description: ").Append(Description).Append("\n");
            sb.Append("  Balance: ").Append(Balance).Append("\n");
            sb.Append("  Dispute: ").Append(Dispute).Append("\n");
            sb.Append("  SelfUrl: ").Append(SelfUrl).Append("\n");
            sb.Append("  AccountUrl: ").Append(AccountUrl).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as Transaction);
        }

        /// <summary>
        /// Returns true if Transaction instances are equal
        /// </summary>
        /// <param name="input">Instance of Transaction to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(Transaction input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Id == input.Id ||
                    (this.Id != null &&
                    this.Id.Equals(input.Id))
                ) && 
                (
                    this.DateTime == input.DateTime ||
                    (this.DateTime != null &&
                    this.DateTime.Equals(input.DateTime))
                ) && 
                (
                    this.Amount == input.Amount ||
                    (this.Amount != null &&
                    this.Amount.Equals(input.Amount))
                ) && 
                (
                    this.TransactionType == input.TransactionType ||
                    (this.TransactionType != null &&
                    this.TransactionType.Equals(input.TransactionType))
                ) && 
                (
                    this.Reference == input.Reference ||
                    (this.Reference != null &&
                    this.Reference.Equals(input.Reference))
                ) && 
                (
                    this.Description == input.Description ||
                    (this.Description != null &&
                    this.Description.Equals(input.Description))
                ) && 
                (
                    this.Balance == input.Balance ||
                    (this.Balance != null &&
                    this.Balance.Equals(input.Balance))
                ) && 
                (
                    this.Dispute == input.Dispute ||
                    (this.Dispute != null &&
                    this.Dispute.Equals(input.Dispute))
                ) && 
                (
                    this.SelfUrl == input.SelfUrl ||
                    (this.SelfUrl != null &&
                    this.SelfUrl.Equals(input.SelfUrl))
                ) && 
                (
                    this.AccountUrl == input.AccountUrl ||
                    (this.AccountUrl != null &&
                    this.AccountUrl.Equals(input.AccountUrl))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.Id != null)
                    hashCode = hashCode * 59 + this.Id.GetHashCode();
                if (this.DateTime != null)
                    hashCode = hashCode * 59 + this.DateTime.GetHashCode();
                if (this.Amount != null)
                    hashCode = hashCode * 59 + this.Amount.GetHashCode();
                if (this.TransactionType != null)
                    hashCode = hashCode * 59 + this.TransactionType.GetHashCode();
                if (this.Reference != null)
                    hashCode = hashCode * 59 + this.Reference.GetHashCode();
                if (this.Description != null)
                    hashCode = hashCode * 59 + this.Description.GetHashCode();
                if (this.Balance != null)
                    hashCode = hashCode * 59 + this.Balance.GetHashCode();
                if (this.Dispute != null)
                    hashCode = hashCode * 59 + this.Dispute.GetHashCode();
                if (this.SelfUrl != null)
                    hashCode = hashCode * 59 + this.SelfUrl.GetHashCode();
                if (this.AccountUrl != null)
                    hashCode = hashCode * 59 + this.AccountUrl.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }
}
