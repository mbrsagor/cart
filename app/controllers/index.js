import Controller from '@ember/controller';
import { match, not } from "@ember/object/computed";

export default Controller.extend({
  responseMessage: "",
  emailAddress: "",
  headerMessage : "Comming Soon",
  headerSubTitle : "Don't miss our launch date, request an invitation now.",

  isValid: match("emailAddress", /^.+@.+\..+$/),
  isDisabled: not("isValid"),
  
  actions: {
    saveInvitation(){
        const email = this.get("emailAddress");
        
        const newInvitation = this.store.createRecord('invitation', { email: email });
        newInvitation.save();
        
        this.set('responseMessage', `Thank you! We have just saved your email address: ${this.get('emailAddress')}`);
        this.set("emailAddress", "");
    }
  }
});
