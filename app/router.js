import EmberRouter from '@ember/routing/router';
import config from './config/environment';

const Router = EmberRouter.extend({
  location: config.locationType,
  rootURL: config.rootURL
});

Router.map(function() {
  this.route('about');
  this.route('contact');

  this.route('admin', function() {
    this.route('seeder');
    this.route('invitations');
    this.route('contacts');
  });
  this.route('libraries', function(){
    this.route('new');
    this.route('edit', {path: '/:library_id/edit'});
  });
  this.route('authors');
  this.route('books');
});

export default Router;
