/*
 * Created by Michael Roberts
 */
package dev.MRobinBatman.UpWork;

public class UpWorkJob {
private String title;
private String url;
private String duration;
private String experience;
private String jobType;
private String postTime;

public UpWorkJob(String aS, String bS, String cS, String dS, String eS, String fS) {
	this.title = aS;
	this.url = bS;
	this.duration = cS;
	this.experience = dS;
	this.jobType = eS;
	this.postTime = fS;
}

public String getTitle() {
	return title;
}

public void setTitle(String title) {
	this.title = title;
}

public String getUrl() {
	return url;
}

public void setUrl(String url) {
	this.url = url;
}

public String getDuration() {
	return duration;
}

public void setDuration(String poster) {
	this.duration = poster;
}

public String getExperience() {
	return experience;
}

public void setExperience(String experience) {
	this.experience = experience;
}

public String getJobType() {
	return jobType;
}

public void setJobType(String jobType) {
	this.jobType = jobType;
}

public String getPostTime() {
	return postTime;
}

public void setPostTime(String postTime) {
	this.postTime = postTime;
}
}
