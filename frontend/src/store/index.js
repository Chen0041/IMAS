import Vuex from 'vuex'

const store = new Vuex.Store({
    state: {
        user: JSON.parse(sessionStorage.getItem("addsCurrentUserInfo")) || {},
        token: sessionStorage.getItem("addsCurrentUserToken") || "",
        sysData: JSON.parse(sessionStorage.getItem("addsSysData")) || {}
    },
    mutations: {
        saveUserInfo(state, userInfo) {
            state.user = userInfo;
            // console.log(state.user);
            // Save "userInfo" to sessionStorage
            sessionStorage.setItem("addsCurrentUserInfo", JSON.stringify(userInfo));
        },
        saveToken(state, token) {
            state.token = token;
            sessionStorage.setItem("addsCurrentUserToken", token);
        },
        saveSysData(state, data) {
            state.sysData = data;
            sessionStorage.setItem("addsSysData", JSON.stringify(data));
        },
        clearUserInfo(state) {
            state.user = {};
            state.token = "";
            state.sysData = {};
            // Remove "userInfo", "token", "sysData" from sessionStorage
            sessionStorage.removeItem("addsCurrentUserInfo");
            sessionStorage.removeItem("addsCurrentUserToken");
            sessionStorage.removeItem("addsSysData");
        },
    },
    actions: {
        saveUserInfo(context, userInfo) {
            context.commit("saveUserInfo", userInfo);
        },
        saveToken(context, token) {
            context.commit("saveToken", token);
        },
        saveSysData(context, data) {
            context.commit("saveSysData", data);
        },
    }
});

export default store;
