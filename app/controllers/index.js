import Controller from '@ember/controller';

export default Controller.extend({
  responseMessage: "",
  emailAddress: "",
  headerMessage: "Comming Soon",
  headerSubTitle: "Don't miss our launch date, request an invitation now.",

  actions: {
    saveInvitation(newInvitation) {
      newInvitation
        .save().then((response) => {
          this.set('responseMessage', true);
          this.set('model.email', '');
          console.log(response)
        })
        .catch((response) => console.log("error:", response));
    },
  },
});
