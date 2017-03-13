#version 330
uniform mat4 model, view, nmat, proj;

uniform int cmode;

in vec3 position_eye;
in vec3 normal_eye;
out vec4 outcolor;

void main()
{
    vec3 color;
    
    switch(cmode)
    {
    case 2:
        color = normal_eye*0.5+0.5;
        break;
    
    case 1:
        color = vec3(.11);
        break;
    
    default:
        const vec3 white = vec3(1.);
        const vec3 yllow = vec3(1.,.6,.0);
        const vec3 lgray = vec3(.8);
        const vec3 mgray = vec3(.5);
        const vec3 dgray = vec3(.2);
        // light
        const vec3 La = white;
        const vec3 Ld = white;
        const vec3 Ls = white;
        // material
        const vec3 Ka = dgray;
        const vec3 Kd = yllow;
        const vec3 Ks = vec3(.7,.2,.0);
        const float spec_exp = 35.0f;
        
        vec3 light_position_eye = vec3(.0,.0,3.);

        vec3 to_light = normalize(light_position_eye-position_eye);
        vec3 to_eye = normalize(-position_eye);
        vec3 normal = normalize(normal_eye);
        vec3 refl = reflect(-to_light,normal);

        float diff_fact = dot(to_light,normal);
        float spec_fact = pow(max(dot(to_eye,refl),.0),spec_exp);
        
        color = La * Ka;
        if( diff_fact > 0 ){
            color += Ld * Kd * diff_fact;
            color += Ls * Ks * spec_fact;
        }
    }// END switch(cmode)
    
    outcolor = vec4(color,1.);
}
