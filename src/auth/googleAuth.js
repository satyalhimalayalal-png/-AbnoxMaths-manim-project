import { CONFIG } from '../config.js';
let tokenClient;
let accessToken = null;
export const initAuth = (onSuccess) => {
    tokenClient = google.accounts.oauth2.initTokenClient({
        client_id: CONFIG.GOOGLE_CLIENT_ID,
        scope: CONFIG.SCOPES,
        callback: (tokenResponse) => {
            if (tokenResponse.access_token) {
                accessToken = tokenResponse.access_token;
                onSuccess(accessToken);
            }
        },
    });
};
export const signIn = () => tokenClient?.requestAccessToken();
export const getAccessToken = () => accessToken;
export const signOut = () => {
    if(accessToken) google.accounts.oauth2.revoke(accessToken);
    accessToken = null;
    location.reload();
};