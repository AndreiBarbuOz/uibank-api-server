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
    /// BankCard
    /// </summary>
    [DataContract]
        public partial class BankCard :  IEquatable<BankCard>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="BankCard" /> class.
        /// </summary>
        /// <param name="id">id.</param>
        /// <param name="dateStart">dateStart.</param>
        /// <param name="dateEnd">dateEnd.</param>
        /// <param name="nameOnCard">nameOnCard.</param>
        /// <param name="pin">pin.</param>
        /// <param name="securityCode">securityCode.</param>
        /// <param name="blocked">blocked.</param>
        /// <param name="selfUrl">selfUrl.</param>
        /// <param name="accountUrl">accountUrl.</param>
        public BankCard(long? id = default(long?), DateTime? dateStart = default(DateTime?), DateTime? dateEnd = default(DateTime?), string nameOnCard = default(string), long? pin = default(long?), string securityCode = default(string), bool? blocked = default(bool?), string selfUrl = default(string), string accountUrl = default(string))
        {
            this.Id = id;
            this.DateStart = dateStart;
            this.DateEnd = dateEnd;
            this.NameOnCard = nameOnCard;
            this.Pin = pin;
            this.SecurityCode = securityCode;
            this.Blocked = blocked;
            this.SelfUrl = selfUrl;
            this.AccountUrl = accountUrl;
        }
        
        /// <summary>
        /// Gets or Sets Id
        /// </summary>
        [DataMember(Name="id", EmitDefaultValue=false)]
        public long? Id { get; set; }

        /// <summary>
        /// Gets or Sets DateStart
        /// </summary>
        [DataMember(Name="date_start", EmitDefaultValue=false)]
        [JsonConverter(typeof(SwaggerDateConverter))]
        public DateTime? DateStart { get; set; }

        /// <summary>
        /// Gets or Sets DateEnd
        /// </summary>
        [DataMember(Name="date_end", EmitDefaultValue=false)]
        [JsonConverter(typeof(SwaggerDateConverter))]
        public DateTime? DateEnd { get; set; }

        /// <summary>
        /// Gets or Sets NameOnCard
        /// </summary>
        [DataMember(Name="name_on_card", EmitDefaultValue=false)]
        public string NameOnCard { get; set; }

        /// <summary>
        /// Gets or Sets Pin
        /// </summary>
        [DataMember(Name="pin", EmitDefaultValue=false)]
        public long? Pin { get; set; }

        /// <summary>
        /// Gets or Sets SecurityCode
        /// </summary>
        [DataMember(Name="security_code", EmitDefaultValue=false)]
        public string SecurityCode { get; set; }

        /// <summary>
        /// Gets or Sets Blocked
        /// </summary>
        [DataMember(Name="blocked", EmitDefaultValue=false)]
        public bool? Blocked { get; set; }

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
            sb.Append("class BankCard {\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("  DateStart: ").Append(DateStart).Append("\n");
            sb.Append("  DateEnd: ").Append(DateEnd).Append("\n");
            sb.Append("  NameOnCard: ").Append(NameOnCard).Append("\n");
            sb.Append("  Pin: ").Append(Pin).Append("\n");
            sb.Append("  SecurityCode: ").Append(SecurityCode).Append("\n");
            sb.Append("  Blocked: ").Append(Blocked).Append("\n");
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
            return this.Equals(input as BankCard);
        }

        /// <summary>
        /// Returns true if BankCard instances are equal
        /// </summary>
        /// <param name="input">Instance of BankCard to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(BankCard input)
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
                    this.DateStart == input.DateStart ||
                    (this.DateStart != null &&
                    this.DateStart.Equals(input.DateStart))
                ) && 
                (
                    this.DateEnd == input.DateEnd ||
                    (this.DateEnd != null &&
                    this.DateEnd.Equals(input.DateEnd))
                ) && 
                (
                    this.NameOnCard == input.NameOnCard ||
                    (this.NameOnCard != null &&
                    this.NameOnCard.Equals(input.NameOnCard))
                ) && 
                (
                    this.Pin == input.Pin ||
                    (this.Pin != null &&
                    this.Pin.Equals(input.Pin))
                ) && 
                (
                    this.SecurityCode == input.SecurityCode ||
                    (this.SecurityCode != null &&
                    this.SecurityCode.Equals(input.SecurityCode))
                ) && 
                (
                    this.Blocked == input.Blocked ||
                    (this.Blocked != null &&
                    this.Blocked.Equals(input.Blocked))
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
                if (this.DateStart != null)
                    hashCode = hashCode * 59 + this.DateStart.GetHashCode();
                if (this.DateEnd != null)
                    hashCode = hashCode * 59 + this.DateEnd.GetHashCode();
                if (this.NameOnCard != null)
                    hashCode = hashCode * 59 + this.NameOnCard.GetHashCode();
                if (this.Pin != null)
                    hashCode = hashCode * 59 + this.Pin.GetHashCode();
                if (this.SecurityCode != null)
                    hashCode = hashCode * 59 + this.SecurityCode.GetHashCode();
                if (this.Blocked != null)
                    hashCode = hashCode * 59 + this.Blocked.GetHashCode();
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
