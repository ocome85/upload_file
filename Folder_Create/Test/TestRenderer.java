package com.nijisanjiworld.nijisanjiworldmod.mobdata.enemy.Test;


import com.nijisanjiworld.nijisanjiworldmod.main.NijisanjiWorldMod;
import net.minecraft.client.model.geom.ModelLayerLocation;
import net.minecraft.client.renderer.entity.EntityRendererProvider;
import net.minecraft.client.renderer.entity.MobRenderer;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.entity.Entity;

import static com.nijisanjiworld.nijisanjiworldmod.main.ModEntityRenderers.*;

public class TestRenderer extends MobRenderer {
    private static final ResourceLocation TEXTURE = new ResourceLocation(NijisanjiWorldMod.MOD_ID, "textures/entity/ars/ars.png");

    public TestRenderer(EntityRendererProvider.Context p_174456_) {
        this(p_174456_, TEST_LAYER);
    }
    public TestRenderer(EntityRendererProvider.Context p_174458_, ModelLayerLocation p_174459_) {
        super(p_174458_, new TestModel<>(p_174458_.bakeLayer(TEST_LAYER)),0.5F);
    }

    @Override
    public ResourceLocation getTextureLocation(Entity p_114482_) {
        return TEXTURE;
    }
}