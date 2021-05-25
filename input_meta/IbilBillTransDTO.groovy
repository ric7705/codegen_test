package com.hcsaastech.ehis.ibil.accountcharge

import com.hcsaastech.common.utility.*

class IbilBillTransDTO extends DTOBase {
	String	caseno			//住院序號
	int	fincnt				//身分分段
	int	billSeqno			//序號
	String	patKind			//收款類別
	BigDecimal	tamt		//金額
	String	feeAccount		//帳號
	Date	feeDate			//日期
	String	feeTime			//時間
	String	handler			//收費員姓名
	String	dischgLocation	//收費地點
	String	recStatus		//狀態
	String	remarks			//備註
	String	createdBy		//建構者
	Date	dateCreated		//建構日
	String	lastUpdatedBy	//異動者
	Date	lastUpdated		//異動日
	//20100319 New by Jeff
	Date	billDate		//收費日期
	String	billTime		//收費時間
	
}
