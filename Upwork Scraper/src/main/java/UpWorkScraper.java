
/*
 * Created by Michael Roberts
 */
import com.gargoylesoftware.htmlunit.WebClient;
import com.gargoylesoftware.htmlunit.html.HtmlPage;
import com.gargoylesoftware.htmlunit.javascript.host.dom.NodeList;

import dev.MRobinBatman.UpWork.*;

import java.util.List;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.gargoylesoftware.htmlunit.*;
import com.gargoylesoftware.htmlunit.html.*;

public class UpWorkScraper {

	public static void main(String args[]) throws Exception {
		String baseUrl = "https://www.upwork.com/freelance-jobs/web-scraping/";

		WebClient client = new WebClient();
		client.getOptions().setCssEnabled(false);
		client.getOptions().setJavaScriptEnabled(false);
		client.getOptions().setUseInsecureSSL(true);

		HtmlPage page = client.getPage(baseUrl);
		System.out.println(page.getTitleText());

		List<HtmlElement> itemList = page.getByXPath("//div[@class='container-visitor']");

		if (itemList.isEmpty()) {
			System.out.println("No Items Found");
		} else {
			System.out.println(itemList);
			for (HtmlElement htmlItem : itemList) {
				String title = ((HtmlElement) htmlItem
						.getFirstByXPath("//a[@class= 'd-block display-u2u job-title h5 mb-10']")).asText();
				String url = ((HtmlElement) htmlItem.getFirstByXPath("//div[@class='mb-20']")).asXml();

				// had trouble getting the part of the url that i wanted, so what i wil do
				// is find the index of the xml that says "href" and substring the url extension
				// from that
				int index = url.indexOf("<a href=\"");
				int index2 = url.indexOf(" data-qa");
				index += 9;
				index2 -= 1;
				url = url.substring(index, index2);
				url = "https://www.upwork.com" + url;
				String duration = "PLACEHOLDER";
//						((HtmlElement) htmlItem.getFirstByXPath("//*[@id=\"main\"]/div/div/div[2]/section[3]/div[1]/div[2]/div[1]/div[1]/section/div[1]/div[2]/p[2]/strong"))
//						.asText();
				String experience = ((HtmlElement) htmlItem.getFirstByXPath(
						"//*[@id=\"main\"]/div/div/div[2]/section[3]/div[1]/div[2]/div[1]/div[1]/section/div[1]/div[2]/p[2]/strong"))
								.asText();
				String jobType = ((HtmlElement) htmlItem.getFirstByXPath(
						"//*[@id=\"main\"]/div/div/div[2]/section[3]/div[1]/div[2]/div[1]/div[1]/section/div[1]/div[1]/small[1]"))
								.asText();
				String postTime = ((HtmlElement) htmlItem.getFirstByXPath(
						"//*[@id=\"main\"]/div/div/div[2]/section[3]/div[1]/div[2]/div[1]/div[1]/section/div[1]/div[1]/small[2]"))
								.asText();
				UpWorkJob uWJ = new UpWorkJob(title, url, duration, experience, jobType, postTime);

				ObjectMapper mapper = new ObjectMapper();
				String jsonString = mapper.writeValueAsString(uWJ);

				System.out.println(jsonString);

			}

		}

	}
}
