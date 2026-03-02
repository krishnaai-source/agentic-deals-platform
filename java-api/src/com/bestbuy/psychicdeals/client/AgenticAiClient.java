// AgenticAiClient.java
package com.bestbuy.psychicdeals.client;

import com.bestbuy.psychicdeals.dto.DealRequest;
import com.bestbuy.psychicdeals.dto.DealResponse;
import org.springframework.stereotype.Component;
import org.springframework.web.reactive.function.client.WebClient;

@Component
public class AgenticAiClient {

    private final WebClient webClient;

    public AgenticAiClient(WebClient.Builder builder) {
        this.webClient = builder.baseUrl("http://agentic-ai:8000").build();
    }

    public DealResponse fetchDeals(DealRequest request) {
        return webClient.post()
                .uri("/agentic/deals")
                .bodyValue(request)
                .retrieve()
                .bodyToMono(DealResponse.class)
                .block();
    }
}
