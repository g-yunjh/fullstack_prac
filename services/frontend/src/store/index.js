import { createStore } from "vuex";

import users from './modules/users';
import posts from './modules/posts';


export default createStore({
  modules: {
    posts,
    users,
  }
});