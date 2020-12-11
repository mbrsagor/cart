import Controller from '@ember/controller';
import { match, not, gte } from "@ember/object/computed";

export default Controller.extend({
  isValid: match("emailAddress", /^.+@.+\..+$/),
  isDisabled: not("isValid"),

  isLongEnough: gte("message.length", 5)
});
