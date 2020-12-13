import DS from 'ember-data';
import fetch from "fetch";

export default DS.JSONAPIAdapter.extend({
    queryRecord(store, type, query) {
    return fetch("http://127.0.0.1:8000/api/librays/");
  }
});
