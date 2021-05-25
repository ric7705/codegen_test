api call sample:
```java
import flex.messaging.io.amf.ASObject;
import java.text.SimpleDateFormat;
import java.util.HashMap;
import java.util.Map;

def logDTO = new ASObject("com.hcsaastech.ehis.ibil.accountcharge.IbilRootBillMDDistMDDTO");
SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss");
Date d;

logDTO["ibilDistMstDTO"] = null;
logDTO["id"] = 0;
logDTO["arrayOfIbilDistDtlDTO"] = null;
logDTO["edition"] = 0;
logDTO["rowStatus"] = null;

Map < String, Object > mp1 = new HashMap < String, Object > ();
mp1.put("patPaidAmt", 0.0);
mp1.put("oeiKind", "I");
mp1.put("patName", "\\u5289\\u5b50\\u921e");
mp1.put("patAmt", 164899);
mp1.put("emgBedDays", 2);
mp1.put("creditAmt", 0.0);
mp1.put("tranSeqno", "1");
mp1.put("cancelOper", null);
mp1.put("fincnt", 1);
mp1.put("totSelfDiscAmt", 0.0);
mp1.put("lastUpdatedBy", null);
mp1.put("dateCreated", "2021-05-07T02:43:34+0000");
mp1.put("id", 3594228);
mp1.put("emgExpAmt1", 160759.0);
mp1.put("chronExpAmt4", 0.0);
mp1.put("edition", 0);
mp1.put("oweAmt", 0.0);
mp1.put("emgExpAmt2", 0.0);
mp1.put("chronPayAmt3", 0.0);
mp1.put("paidType", "1");
mp1.put("lastUpdated", "2021-05-07T02:43:34+0000");
mp1.put("chronPayAmt1", 0.0);
mp1.put("chronExpAmt1", 0.0);
mp1.put("caseno", "I21050377");
mp1.put("chronBedDays", 0);
mp1.put("patEngName", "\\u5289\\u5b50\\u921e");
mp1.put("delSeqno", "1");
mp1.put("totGlDiscAmt", 0.0);
mp1.put("chronExpAmt3", 0.0);
mp1.put("emgPayAmt1", 16076.0);
mp1.put("emgExpAmt4", 0.0);
mp1.put("emgPayAmt4", 0.0);
mp1.put("rowStatus", "R");
mp1.put("billSeqno", "1");
mp1.put("prePaidAmt", 20216.0);
mp1.put("hosted", "bill");
mp1.put("emgExpAmt3", 0.0);
mp1.put("discAmt", 0.0);
mp1.put("subsidyAmt", 0.0);
mp1.put("emgPayAmt3", 0.0);
mp1.put("chartNo", "701053948");
mp1.put("edDate", "2021-05-07T02:15:00+0000");
mp1.put("emgPayAmt2", 0.0);
mp1.put("chronExpAmt2", 0.0);
mp1.put("actStatus", "N");
mp1.put("totGlAmt", 4140.0);
mp1.put("chronPayAmt2", 0.0);
mp1.put("billAmt", 0.0);
mp1.put("discUnit", null);
mp1.put("stDate", "2021-05-05T02:28:16+0000");
mp1.put("paidStatus", "N");
mp1.put("billKind", "1");
mp1.put("printerId", "20");
mp1.put("totSelfAmt", 16076.0);
mp1.put("billCheckKind", "N");
mp1.put("patKind", "1");
mp1.put("patSelfAmt", 16076.0);
mp1.put("chronPayAmt4", 0.0);
mp1.put("patId", "1");
mp1.put("handler", "ibil");
mp1.put("closeOper", null);
mp1.put("paidDate", "2021-05-07T02:43:34+0000");
mp1.put("issueDate", "2021-05-07T02:43:34+0000");
mp1.put("totDistAmt", 0.0);
mp1.put("remarks", null);
mp1.put("createdBy", "ibil");
mp1.put("cancelDate", null);
mp1.put("paidFlag", "Y");
mp1.put("totAmt", 20216.0);
mp1.put("recStatus", "N");
mp1.put("closeDate", "2021-05-07T02:43:34+0000");

Map < String, Object > mp2 = new HashMap < String, Object > ();
mp2.put("fincnt", 1);
mp2.put("lastUpdatedBy", "000021826");
mp2.put("dateCreated", "2021-05-07T02:45:27+0000");
mp2.put("id", 0);
mp2.put("tamt", 0.0);
mp2.put("edition", 0);
mp2.put("feeAccount", "701053948");
mp2.put("dischgLocation", "");
mp2.put("lastUpdated", "2021-05-07T02:45:27+0000");
mp2.put("patKind", "12");
mp2.put("caseno", "I21050377");
mp2.put("feeDate", "2021-05-07T02:45:01+0000");
mp2.put("handler", "\\u767d\\u601d\\u654f");
mp2.put("remarks", "");
mp2.put("billDate", "2021-05-07T02:44:39+0000");
mp2.put("createdBy", "000021826");
mp2.put("billTime", "1044");
mp2.put("rowStatus", "C");
mp2.put("billSeqno", 0);
mp2.put("feeTime", "1045");
mp2.put("recStatus", "N");
logDTO["ibilBillmstDTO"] = mp1
logDTO["arrayOfIbilBillTransDTO"] = [mp2]

parameters["ibilRootData"] = ["I21050377", "BB", null, null, "000021826", "10.2.74.81", "I"];

parameters["ibilRootBillMDDistMDDTO"] = logDTO
```