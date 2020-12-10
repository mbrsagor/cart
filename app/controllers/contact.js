import { and } from "@ember/object/computed";
import Controller from '@ember/controller';

export default Controller.extend({
  isBothTrue: and("firstComputedProperty", "secondComputedProperty"),
});
