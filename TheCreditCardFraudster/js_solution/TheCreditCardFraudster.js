const karta = "543210******1234";
	const karta_test = "7155032979402154";

	function luhn(nr)
	{
		
		let iloczyn = 0;
		let suma = 0;

		for(let i=nr.length-1; i>=0; i--)
		{
			if(i%2)
				{
					suma+=parseInt(nr.charAt(i));
				}
			else
				{
					iloczyn = parseInt(nr.charAt(i)) * 2;
					if(iloczyn>9)
					{
						//iloczyn = iloczyn%10 + 10;
						iloczyn -= 9;
					}
					suma+=iloczyn;
					iloczyn = 0;
				}
		}

		return suma;
	}

	function search_six(nr)
	{
		const must_modulo = 123457;
		let guess = 0;
		let test = ""
		for(let i=0; i<=999999; i++)
		{
			guess = i.toString().padStart(6, "0");
			test = nr.substr(0, 6) + guess + nr.substr(12);

			if( (parseInt(test)%must_modulo==0) && (luhn(test)%10==0) )
			{
				return test;
			}
		}
	}

	//document.querySelector(".pojemnik").innerHTML = luhn(karta_test);
	document.querySelector(".pojemnik").innerHTML = search_six(karta);
 