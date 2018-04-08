package com.andy.psu.smsgateway;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;
import org.json.JSONObject;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.telephony.SmsManager;
import android.telephony.SmsMessage;
import android.util.Log;

public class IncomingSms extends BroadcastReceiver {
	final SmsManager sms = SmsManager.getDefault();
	private static final String LOG_TAG = "PSUSMSGATEWAY";
	
	public void onReceive(Context context, Intent intent) {
	
		final Bundle bundle = intent.getExtras();
		
		try {
			if (bundle != null) {
				
				final Object[] pdusObj = (Object[]) bundle.get("pdus"); 
				
				for (int i = 0; i < pdusObj.length; ++i) {
					
					SmsMessage currentMessage = SmsMessage.createFromPdu((byte[]) pdusObj[i]);
					String phoneNumber = currentMessage.getDisplayOriginatingAddress();
					
			        String senderNum = phoneNumber;
			        String message = currentMessage.getDisplayMessageBody();

			        // handle message from foolish people
			        // trim
			        message = message.trim();
			        
			        //check out our digits
			        if (message.matches("\\d+")) // только числа принимаем, ничего не режем
			        {
			        	String sHostname = BroadcastSms.getHostname();
			        	// vote
			        	// send poll, option and number
			        	// poll we got only one,
			        	// option's parsed from the message
			        	// and number from sendNumber
			        	new SetJSONTask(message,phoneNumber,"http://" + sHostname+"/vote.php").execute();
			        }
			        else
			        {
			        	Log.i(LOG_TAG, "onReceive>WRONG NUMBER: " + message +" from number: " + senderNum);
			        }
			        
			        Log.i(LOG_TAG, "onReceive>senderNumber: " + senderNum + "; message: " + message);
				}
              }
		} catch (Exception e) {
			Log.e(LOG_TAG, "onReceive>Exception smsReceiver" + e );
		}
	}
	
	class SetJSONTask extends AsyncTask<String, Void, JSONObject> {
        private String poll, optionID, number, host;
        
		public SetJSONTask(String optionID, String number, String host) {
        	this.optionID = optionID;
        	this.number = number;
        	this.host = host;
        	this.poll="1";
		}

		@Override
		protected JSONObject doInBackground(String... urls) {
            try {
            	HttpClient httpclient = new DefaultHttpClient();
                HttpPost httppost = new HttpPost(this.host);

                try {
                    List<NameValuePair> nameValuePairs = new ArrayList<NameValuePair>(2);
                    nameValuePairs.add(new BasicNameValuePair("poll", this.poll));
                    nameValuePairs.add(new BasicNameValuePair("option", this.optionID));
                    nameValuePairs.add(new BasicNameValuePair("number", this.number));
                    httppost.setEntity(new UrlEncodedFormEntity(nameValuePairs));

                    HttpResponse response = httpclient.execute(httppost);
                    String s = response.getStatusLine().toString();
                    Log.e(LOG_TAG, "SetJSONTask>doInBackground>STTAUS " + s);
                } catch (ClientProtocolException e) {
                	Log.e(LOG_TAG, "SetJSONTask>doInBackground>Exception " + e);
                } catch (IOException e) {
                	Log.e(LOG_TAG, "SetJSONTask>doInBackground>Exception " + e);
                }
            } catch (Exception e) {
                return null;
            }
			return null;
        }
    }
}