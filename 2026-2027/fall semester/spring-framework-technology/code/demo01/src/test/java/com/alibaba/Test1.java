package com.alibaba;

import com.alibaba.service.UserService;
import lombok.RequiredArgsConstructor;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.mock.web.MockHttpServletResponse;
import org.springframework.test.context.TestConstructor;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.MvcResult;
import org.springframework.test.web.servlet.ResultActions;
import org.springframework.test.web.servlet.request.MockHttpServletRequestBuilder;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;

@TestConstructor(autowireMode = TestConstructor.AutowireMode.ALL)
@RequiredArgsConstructor
@AutoConfigureMockMvc
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
public class Test1 {

    private final MockMvc mvc;

    @Test
    void testWeb(@Autowired MockMvc mvc) throws Exception {

    }

    @Test
    void testWeb2() throws Exception {
        // 模拟创建一个虚拟请求 打到 /port 这个url上去
        MockHttpServletRequestBuilder builder = MockMvcRequestBuilders.get("/api/test/hello");
        ;
        // 执行这个请求对应的的方法
        ResultActions resultActions = mvc.perform(builder);

        // 1. 拿到 MvcResult
        MvcResult mvcResult = resultActions.andReturn();

        // 2. 拿到 MockHttpServletResponse
        MockHttpServletResponse response = mvcResult.getResponse();

        // 3. 取各种返回值
        String body = response.getContentAsString();          // 响应体（字符串）
        int status = response.getStatus();                    // 状态码 200
        String contentType = response.getContentType();       // Content-Type
        System.out.println(body);
    }

    @Test
    void testWeb3() throws Exception {
        // 模拟创建一个虚拟请求 打到 /port 这个url上去
        MockHttpServletRequestBuilder builder = MockMvcRequestBuilders.get("/api/user/info");
        ;
        // 执行这个请求对应的的方法
        ResultActions resultActions = mvc.perform(builder);
        System.out.println("123");
    }

    private final UserService userService;

    @Test
    void testWeb4() throws Exception {
        String result = userService.getUserId(Long.valueOf(666));
        System.out.println("当前的用户id是：" + result);
    }

}
