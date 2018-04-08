package com.andy.psu.smsgateway;

import org.json.JSONException;
import org.json.JSONObject;

import com.andy.psu.smsgateway.R;

import android.app.Activity;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.EditText;

public class BroadcastSms extends Activity {
	
	EditText tvHost;
	Button btnLock;
	boolean btnIsLocked = false;
	private static String sHost = "";
	
	public static String getHostname() {
		return sHost;
	}
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.broadcast_sms);
		
		getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
		
		final Button clickButton = (Button) findViewById(R.id.button_sql_check);
		this.tvHost = (EditText) findViewById(R.id.et_sql);
		this.btnLock = (Button) findViewById(R.id.button_sql_lock);
		clickButton.setBackgroundColor(0xAAFF0000);
		btnLock.setBackgroundColor(0xAAFF0000);
		
		clickButton.setOnClickListener( new OnClickListener() {
		            @Override
		            public void onClick(View v) {
		            	GetJSONTask gjt = new GetJSONTask(clickButton);
		            	String host = tvHost.getText().toString();
		            	gjt.execute("http://" + host +"/?check");
		            }
		        });
		
		btnLock.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
            	if (btnIsLocked)
            	{
            		btnLock.setBackgroundColor(0xAAFF0000);
            		btnIsLocked = false;
            		tvHost.setFocusableInTouchMode(true);
            	}
            	else {
            		btnLock.setBackgroundColor(0xAA00FF00);
            		btnIsLocked = true;
            		tvHost.setFocusable(false);
            		sHost = tvHost.getText().toString();
            	}
            }
        });
	}
	
	 // данные из проверки
	class GetJSONTask extends AsyncTask<String, Void, JSONObject> {
        public GetJSONTask(Button clickButton) {
        	this.clickButton= clickButton; 
		}

		protected JSONObject doInBackground(String... urls) {
            try {
                JsonParser jParser = new JsonParser();
                JSONObject jo = jParser.getJSONFromUrl(urls[0]);
                if (jo == null) {
                	clickButton.setBackgroundColor(0xAAFF0000);
                }
                return jo;
            } catch (Exception e) {
                return null;
            }
        }

        Button clickButton = null;
        
        protected void onPostExecute(JSONObject json) {
        	boolean bEstablished = false;
        	if (json!=null)
        	{
        		try {
					bEstablished = json.getBoolean("dbconn");
					
					if (bEstablished)
					{
						clickButton.setBackgroundColor(0xAA00FF00);
					}
					
				} catch (JSONException e) {
					e.printStackTrace();
				}
        	} else
        	{
        		Log.i("PSUSMSGATEWAY", ">onPostExecute Json -> NULL");
        	}
        	
        	if (!bEstablished) {
        		clickButton.setBackgroundColor(0xAAFF0000);
        	}
        }
    }
}
