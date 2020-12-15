import DS from 'ember-data';
const { Model } = DS;
import { and, gte, match, not } from "@ember/object/computed";

export default Model.extend({
  email: DS.attr('string'),
  message: DS.attr('string'),
  
  isValidEmail: match('email', /^.+@.+\..+$/),
  isMessageLongEnough: gte('message.length', 5),
  
  isValid: and('isValidEmail', 'isMessageLongEnough'),
  isNotValid: not('isValid')
  
});
