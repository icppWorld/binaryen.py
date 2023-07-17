import cffi

ffibuilder = cffi.FFI()
ffibuilder.set_source("_binaryen_cffi", None)

# cpp -nostdinc -E -P /usr/include/binaryen-c.h > binaryen-py.h
# Remove all deprecated
# format clang-format -style "{BasedOnStyle: llvm, ColumnLimit: 0, AlignAfterOpenBracket: BlockIndent}" binaryen-py.h

ffibuilder.cdef("""
typedef uint32_t BinaryenIndex;
typedef uintptr_t BinaryenType;
BinaryenType BinaryenTypeNone(void);
BinaryenType BinaryenTypeInt32(void);
BinaryenType BinaryenTypeInt64(void);
BinaryenType BinaryenTypeFloat32(void);
BinaryenType BinaryenTypeFloat64(void);
BinaryenType BinaryenTypeVec128(void);
BinaryenType BinaryenTypeFuncref(void);
BinaryenType BinaryenTypeExternref(void);
BinaryenType BinaryenTypeAnyref(void);
BinaryenType BinaryenTypeEqref(void);
BinaryenType BinaryenTypeI31ref(void);
BinaryenType BinaryenTypeStructref(void);
BinaryenType BinaryenTypeArrayref(void);
BinaryenType BinaryenTypeStringref(void);
BinaryenType BinaryenTypeStringviewWTF8(void);
BinaryenType BinaryenTypeStringviewWTF16(void);
BinaryenType BinaryenTypeStringviewIter(void);
BinaryenType BinaryenTypeNullref(void);
BinaryenType BinaryenTypeNullExternref(void);
BinaryenType BinaryenTypeNullFuncref(void);
BinaryenType BinaryenTypeUnreachable(void);
BinaryenType BinaryenTypeAuto(void);
BinaryenType BinaryenTypeCreate(BinaryenType *valueTypes,
                                BinaryenIndex numTypes);
uint32_t BinaryenTypeArity(BinaryenType t);
void BinaryenTypeExpand(BinaryenType t, BinaryenType *buf);
typedef uint32_t BinaryenPackedType;
BinaryenPackedType BinaryenPackedTypeNotPacked(void);
BinaryenPackedType BinaryenPackedTypeInt8(void);
BinaryenPackedType BinaryenPackedTypeInt16(void);
typedef uintptr_t BinaryenHeapType;
BinaryenHeapType BinaryenHeapTypeExt(void);
BinaryenHeapType BinaryenHeapTypeFunc(void);
BinaryenHeapType BinaryenHeapTypeAny(void);
BinaryenHeapType BinaryenHeapTypeEq(void);
BinaryenHeapType BinaryenHeapTypeI31(void);
BinaryenHeapType BinaryenHeapTypeStruct(void);
BinaryenHeapType BinaryenHeapTypeArray(void);
BinaryenHeapType BinaryenHeapTypeString(void);
BinaryenHeapType BinaryenHeapTypeStringviewWTF8(void);
BinaryenHeapType BinaryenHeapTypeStringviewWTF16(void);
BinaryenHeapType BinaryenHeapTypeStringviewIter(void);
BinaryenHeapType BinaryenHeapTypeNone(void);
BinaryenHeapType BinaryenHeapTypeNoext(void);
BinaryenHeapType BinaryenHeapTypeNofunc(void);
bool BinaryenHeapTypeIsBasic(BinaryenHeapType heapType);
bool BinaryenHeapTypeIsSignature(BinaryenHeapType heapType);
bool BinaryenHeapTypeIsStruct(BinaryenHeapType heapType);
bool BinaryenHeapTypeIsArray(BinaryenHeapType heapType);
bool BinaryenHeapTypeIsBottom(BinaryenHeapType heapType);
BinaryenHeapType
BinaryenHeapTypeGetBottom(BinaryenHeapType heapType);
bool BinaryenHeapTypeIsSubType(BinaryenHeapType left,
                               BinaryenHeapType right);
BinaryenIndex
BinaryenStructTypeGetNumFields(BinaryenHeapType heapType);
BinaryenType
BinaryenStructTypeGetFieldType(BinaryenHeapType heapType, BinaryenIndex index);
BinaryenPackedType BinaryenStructTypeGetFieldPackedType(
    BinaryenHeapType heapType, BinaryenIndex index);
bool BinaryenStructTypeIsFieldMutable(BinaryenHeapType heapType,
                                      BinaryenIndex index);
BinaryenType
BinaryenArrayTypeGetElementType(BinaryenHeapType heapType);
BinaryenPackedType
BinaryenArrayTypeGetElementPackedType(BinaryenHeapType heapType);
bool BinaryenArrayTypeIsElementMutable(BinaryenHeapType heapType);
BinaryenType
BinaryenSignatureTypeGetParams(BinaryenHeapType heapType);
BinaryenType
BinaryenSignatureTypeGetResults(BinaryenHeapType heapType);
BinaryenHeapType BinaryenTypeGetHeapType(BinaryenType type);
bool BinaryenTypeIsNullable(BinaryenType type);
BinaryenType BinaryenTypeFromHeapType(BinaryenHeapType heapType,
                                      bool nullable);
typedef uint32_t BinaryenExpressionId;
BinaryenExpressionId BinaryenInvalidId(void);
BinaryenExpressionId BinaryenNopId(void);
;
BinaryenExpressionId BinaryenBlockId(void);
;
BinaryenExpressionId BinaryenIfId(void);
;
BinaryenExpressionId BinaryenLoopId(void);
;
BinaryenExpressionId BinaryenBreakId(void);
;
BinaryenExpressionId BinaryenSwitchId(void);
;
BinaryenExpressionId BinaryenCallId(void);
;
BinaryenExpressionId BinaryenCallIndirectId(void);
;
BinaryenExpressionId BinaryenLocalGetId(void);
;
BinaryenExpressionId BinaryenLocalSetId(void);
;
BinaryenExpressionId BinaryenGlobalGetId(void);
;
BinaryenExpressionId BinaryenGlobalSetId(void);
;
BinaryenExpressionId BinaryenLoadId(void);
;
BinaryenExpressionId BinaryenStoreId(void);
;
BinaryenExpressionId BinaryenAtomicRMWId(void);
;
BinaryenExpressionId BinaryenAtomicCmpxchgId(void);
;
BinaryenExpressionId BinaryenAtomicWaitId(void);
;
BinaryenExpressionId BinaryenAtomicNotifyId(void);
;
BinaryenExpressionId BinaryenAtomicFenceId(void);
;
BinaryenExpressionId BinaryenSIMDExtractId(void);
;
BinaryenExpressionId BinaryenSIMDReplaceId(void);
;
BinaryenExpressionId BinaryenSIMDShuffleId(void);
;
BinaryenExpressionId BinaryenSIMDTernaryId(void);
;
BinaryenExpressionId BinaryenSIMDShiftId(void);
;
BinaryenExpressionId BinaryenSIMDLoadId(void);
;
BinaryenExpressionId BinaryenSIMDLoadStoreLaneId(void);
;
BinaryenExpressionId BinaryenMemoryInitId(void);
;
BinaryenExpressionId BinaryenDataDropId(void);
;
BinaryenExpressionId BinaryenMemoryCopyId(void);
;
BinaryenExpressionId BinaryenMemoryFillId(void);
;
BinaryenExpressionId BinaryenConstId(void);
;
BinaryenExpressionId BinaryenUnaryId(void);
;
BinaryenExpressionId BinaryenBinaryId(void);
;
BinaryenExpressionId BinaryenSelectId(void);
;
BinaryenExpressionId BinaryenDropId(void);
;
BinaryenExpressionId BinaryenReturnId(void);
;
BinaryenExpressionId BinaryenMemorySizeId(void);
;
BinaryenExpressionId BinaryenMemoryGrowId(void);
;
BinaryenExpressionId BinaryenUnreachableId(void);
;
BinaryenExpressionId BinaryenPopId(void);
;
BinaryenExpressionId BinaryenRefNullId(void);
;
BinaryenExpressionId BinaryenRefIsNullId(void);
;
BinaryenExpressionId BinaryenRefFuncId(void);
;
BinaryenExpressionId BinaryenRefEqId(void);
;
BinaryenExpressionId BinaryenTableGetId(void);
;
BinaryenExpressionId BinaryenTableSetId(void);
;
BinaryenExpressionId BinaryenTableSizeId(void);
;
BinaryenExpressionId BinaryenTableGrowId(void);
;
BinaryenExpressionId BinaryenTryId(void);
;
BinaryenExpressionId BinaryenThrowId(void);
;
BinaryenExpressionId BinaryenRethrowId(void);
;
BinaryenExpressionId BinaryenTupleMakeId(void);
;
BinaryenExpressionId BinaryenTupleExtractId(void);
;
BinaryenExpressionId BinaryenI31NewId(void);
;
BinaryenExpressionId BinaryenI31GetId(void);
;
BinaryenExpressionId BinaryenCallRefId(void);
;
BinaryenExpressionId BinaryenRefTestId(void);
;
BinaryenExpressionId BinaryenRefCastId(void);
;
BinaryenExpressionId BinaryenBrOnId(void);
;
BinaryenExpressionId BinaryenStructNewId(void);
;
BinaryenExpressionId BinaryenStructGetId(void);
;
BinaryenExpressionId BinaryenStructSetId(void);
;
BinaryenExpressionId BinaryenArrayNewId(void);
;
BinaryenExpressionId BinaryenArrayNewDataId(void);
;
BinaryenExpressionId BinaryenArrayNewElemId(void);
;
BinaryenExpressionId BinaryenArrayNewFixedId(void);
;
BinaryenExpressionId BinaryenArrayGetId(void);
;
BinaryenExpressionId BinaryenArraySetId(void);
;
BinaryenExpressionId BinaryenArrayLenId(void);
;
BinaryenExpressionId BinaryenArrayCopyId(void);
;
BinaryenExpressionId BinaryenArrayFillId(void);
;
BinaryenExpressionId BinaryenArrayInitDataId(void);
;
BinaryenExpressionId BinaryenArrayInitElemId(void);
;
BinaryenExpressionId BinaryenRefAsId(void);
;
BinaryenExpressionId BinaryenStringNewId(void);
;
BinaryenExpressionId BinaryenStringConstId(void);
;
BinaryenExpressionId BinaryenStringMeasureId(void);
;
BinaryenExpressionId BinaryenStringEncodeId(void);
;
BinaryenExpressionId BinaryenStringConcatId(void);
;
BinaryenExpressionId BinaryenStringEqId(void);
;
BinaryenExpressionId BinaryenStringAsId(void);
;
BinaryenExpressionId BinaryenStringWTF8AdvanceId(void);
;
BinaryenExpressionId BinaryenStringWTF16GetId(void);
;
BinaryenExpressionId BinaryenStringIterNextId(void);
;
BinaryenExpressionId BinaryenStringIterMoveId(void);
;
BinaryenExpressionId BinaryenStringSliceWTFId(void);
;
BinaryenExpressionId BinaryenStringSliceIterId(void);
;
typedef uint32_t BinaryenExternalKind;
BinaryenExternalKind BinaryenExternalFunction(void);
BinaryenExternalKind BinaryenExternalTable(void);
BinaryenExternalKind BinaryenExternalMemory(void);
BinaryenExternalKind BinaryenExternalGlobal(void);
BinaryenExternalKind BinaryenExternalTag(void);
typedef uint32_t BinaryenFeatures;
BinaryenFeatures BinaryenFeatureMVP(void);
BinaryenFeatures BinaryenFeatureAtomics(void);
BinaryenFeatures BinaryenFeatureBulkMemory(void);
BinaryenFeatures BinaryenFeatureMutableGlobals(void);
BinaryenFeatures BinaryenFeatureNontrappingFPToInt(void);
BinaryenFeatures BinaryenFeatureSignExt(void);
BinaryenFeatures BinaryenFeatureSIMD128(void);
BinaryenFeatures BinaryenFeatureExceptionHandling(void);
BinaryenFeatures BinaryenFeatureTailCall(void);
BinaryenFeatures BinaryenFeatureReferenceTypes(void);
BinaryenFeatures BinaryenFeatureMultivalue(void);
BinaryenFeatures BinaryenFeatureGC(void);
BinaryenFeatures BinaryenFeatureMemory64(void);
BinaryenFeatures BinaryenFeatureRelaxedSIMD(void);
BinaryenFeatures BinaryenFeatureExtendedConst(void);
BinaryenFeatures BinaryenFeatureStrings(void);
BinaryenFeatures BinaryenFeatureMultiMemories(void);
BinaryenFeatures BinaryenFeatureAll(void);
typedef struct BinaryenModule *BinaryenModuleRef;
;
BinaryenModuleRef BinaryenModuleCreate(void);
void BinaryenModuleDispose(BinaryenModuleRef module);
struct BinaryenLiteralOLD
{
  uintptr_t type;
  union
  {
    int32_t i32;
    int64_t i64;
    float f32;
    double f64;
    uint8_t v128[16];
    const char *func;
  };
};
struct BinaryenLiteral
{
  uintptr_t type;
  uint8_t v128[16];
};
struct BinaryenLiteral BinaryenLiteralInt32(int32_t x);
struct BinaryenLiteral BinaryenLiteralInt64(int64_t x);
struct BinaryenLiteral BinaryenLiteralFloat32(float x);
struct BinaryenLiteral BinaryenLiteralFloat64(double x);
struct BinaryenLiteral BinaryenLiteralVec128(const uint8_t x[16]);
struct BinaryenLiteral BinaryenLiteralFloat32Bits(int32_t x);
struct BinaryenLiteral BinaryenLiteralFloat64Bits(int64_t x);
typedef int32_t BinaryenOp;
BinaryenOp BinaryenClzInt32(void);
BinaryenOp BinaryenCtzInt32(void);
BinaryenOp BinaryenPopcntInt32(void);
BinaryenOp BinaryenNegFloat32(void);
BinaryenOp BinaryenAbsFloat32(void);
BinaryenOp BinaryenCeilFloat32(void);
BinaryenOp BinaryenFloorFloat32(void);
BinaryenOp BinaryenTruncFloat32(void);
BinaryenOp BinaryenNearestFloat32(void);
BinaryenOp BinaryenSqrtFloat32(void);
BinaryenOp BinaryenEqZInt32(void);
BinaryenOp BinaryenClzInt64(void);
BinaryenOp BinaryenCtzInt64(void);
BinaryenOp BinaryenPopcntInt64(void);
BinaryenOp BinaryenNegFloat64(void);
BinaryenOp BinaryenAbsFloat64(void);
BinaryenOp BinaryenCeilFloat64(void);
BinaryenOp BinaryenFloorFloat64(void);
BinaryenOp BinaryenTruncFloat64(void);
BinaryenOp BinaryenNearestFloat64(void);
BinaryenOp BinaryenSqrtFloat64(void);
BinaryenOp BinaryenEqZInt64(void);
BinaryenOp BinaryenExtendSInt32(void);
BinaryenOp BinaryenExtendUInt32(void);
BinaryenOp BinaryenWrapInt64(void);
BinaryenOp BinaryenTruncSFloat32ToInt32(void);
BinaryenOp BinaryenTruncSFloat32ToInt64(void);
BinaryenOp BinaryenTruncUFloat32ToInt32(void);
BinaryenOp BinaryenTruncUFloat32ToInt64(void);
BinaryenOp BinaryenTruncSFloat64ToInt32(void);
BinaryenOp BinaryenTruncSFloat64ToInt64(void);
BinaryenOp BinaryenTruncUFloat64ToInt32(void);
BinaryenOp BinaryenTruncUFloat64ToInt64(void);
BinaryenOp BinaryenReinterpretFloat32(void);
BinaryenOp BinaryenReinterpretFloat64(void);
BinaryenOp BinaryenConvertSInt32ToFloat32(void);
BinaryenOp BinaryenConvertSInt32ToFloat64(void);
BinaryenOp BinaryenConvertUInt32ToFloat32(void);
BinaryenOp BinaryenConvertUInt32ToFloat64(void);
BinaryenOp BinaryenConvertSInt64ToFloat32(void);
BinaryenOp BinaryenConvertSInt64ToFloat64(void);
BinaryenOp BinaryenConvertUInt64ToFloat32(void);
BinaryenOp BinaryenConvertUInt64ToFloat64(void);
BinaryenOp BinaryenPromoteFloat32(void);
BinaryenOp BinaryenDemoteFloat64(void);
BinaryenOp BinaryenReinterpretInt32(void);
BinaryenOp BinaryenReinterpretInt64(void);
BinaryenOp BinaryenExtendS8Int32(void);
BinaryenOp BinaryenExtendS16Int32(void);
BinaryenOp BinaryenExtendS8Int64(void);
BinaryenOp BinaryenExtendS16Int64(void);
BinaryenOp BinaryenExtendS32Int64(void);
BinaryenOp BinaryenAddInt32(void);
BinaryenOp BinaryenSubInt32(void);
BinaryenOp BinaryenMulInt32(void);
BinaryenOp BinaryenDivSInt32(void);
BinaryenOp BinaryenDivUInt32(void);
BinaryenOp BinaryenRemSInt32(void);
BinaryenOp BinaryenRemUInt32(void);
BinaryenOp BinaryenAndInt32(void);
BinaryenOp BinaryenOrInt32(void);
BinaryenOp BinaryenXorInt32(void);
BinaryenOp BinaryenShlInt32(void);
BinaryenOp BinaryenShrUInt32(void);
BinaryenOp BinaryenShrSInt32(void);
BinaryenOp BinaryenRotLInt32(void);
BinaryenOp BinaryenRotRInt32(void);
BinaryenOp BinaryenEqInt32(void);
BinaryenOp BinaryenNeInt32(void);
BinaryenOp BinaryenLtSInt32(void);
BinaryenOp BinaryenLtUInt32(void);
BinaryenOp BinaryenLeSInt32(void);
BinaryenOp BinaryenLeUInt32(void);
BinaryenOp BinaryenGtSInt32(void);
BinaryenOp BinaryenGtUInt32(void);
BinaryenOp BinaryenGeSInt32(void);
BinaryenOp BinaryenGeUInt32(void);
BinaryenOp BinaryenAddInt64(void);
BinaryenOp BinaryenSubInt64(void);
BinaryenOp BinaryenMulInt64(void);
BinaryenOp BinaryenDivSInt64(void);
BinaryenOp BinaryenDivUInt64(void);
BinaryenOp BinaryenRemSInt64(void);
BinaryenOp BinaryenRemUInt64(void);
BinaryenOp BinaryenAndInt64(void);
BinaryenOp BinaryenOrInt64(void);
BinaryenOp BinaryenXorInt64(void);
BinaryenOp BinaryenShlInt64(void);
BinaryenOp BinaryenShrUInt64(void);
BinaryenOp BinaryenShrSInt64(void);
BinaryenOp BinaryenRotLInt64(void);
BinaryenOp BinaryenRotRInt64(void);
BinaryenOp BinaryenEqInt64(void);
BinaryenOp BinaryenNeInt64(void);
BinaryenOp BinaryenLtSInt64(void);
BinaryenOp BinaryenLtUInt64(void);
BinaryenOp BinaryenLeSInt64(void);
BinaryenOp BinaryenLeUInt64(void);
BinaryenOp BinaryenGtSInt64(void);
BinaryenOp BinaryenGtUInt64(void);
BinaryenOp BinaryenGeSInt64(void);
BinaryenOp BinaryenGeUInt64(void);
BinaryenOp BinaryenAddFloat32(void);
BinaryenOp BinaryenSubFloat32(void);
BinaryenOp BinaryenMulFloat32(void);
BinaryenOp BinaryenDivFloat32(void);
BinaryenOp BinaryenCopySignFloat32(void);
BinaryenOp BinaryenMinFloat32(void);
BinaryenOp BinaryenMaxFloat32(void);
BinaryenOp BinaryenEqFloat32(void);
BinaryenOp BinaryenNeFloat32(void);
BinaryenOp BinaryenLtFloat32(void);
BinaryenOp BinaryenLeFloat32(void);
BinaryenOp BinaryenGtFloat32(void);
BinaryenOp BinaryenGeFloat32(void);
BinaryenOp BinaryenAddFloat64(void);
BinaryenOp BinaryenSubFloat64(void);
BinaryenOp BinaryenMulFloat64(void);
BinaryenOp BinaryenDivFloat64(void);
BinaryenOp BinaryenCopySignFloat64(void);
BinaryenOp BinaryenMinFloat64(void);
BinaryenOp BinaryenMaxFloat64(void);
BinaryenOp BinaryenEqFloat64(void);
BinaryenOp BinaryenNeFloat64(void);
BinaryenOp BinaryenLtFloat64(void);
BinaryenOp BinaryenLeFloat64(void);
BinaryenOp BinaryenGtFloat64(void);
BinaryenOp BinaryenGeFloat64(void);
BinaryenOp BinaryenAtomicRMWAdd(void);
BinaryenOp BinaryenAtomicRMWSub(void);
BinaryenOp BinaryenAtomicRMWAnd(void);
BinaryenOp BinaryenAtomicRMWOr(void);
BinaryenOp BinaryenAtomicRMWXor(void);
BinaryenOp BinaryenAtomicRMWXchg(void);
BinaryenOp BinaryenTruncSatSFloat32ToInt32(void);
BinaryenOp BinaryenTruncSatSFloat32ToInt64(void);
BinaryenOp BinaryenTruncSatUFloat32ToInt32(void);
BinaryenOp BinaryenTruncSatUFloat32ToInt64(void);
BinaryenOp BinaryenTruncSatSFloat64ToInt32(void);
BinaryenOp BinaryenTruncSatSFloat64ToInt64(void);
BinaryenOp BinaryenTruncSatUFloat64ToInt32(void);
BinaryenOp BinaryenTruncSatUFloat64ToInt64(void);
BinaryenOp BinaryenSplatVecI8x16(void);
BinaryenOp BinaryenExtractLaneSVecI8x16(void);
BinaryenOp BinaryenExtractLaneUVecI8x16(void);
BinaryenOp BinaryenReplaceLaneVecI8x16(void);
BinaryenOp BinaryenSplatVecI16x8(void);
BinaryenOp BinaryenExtractLaneSVecI16x8(void);
BinaryenOp BinaryenExtractLaneUVecI16x8(void);
BinaryenOp BinaryenReplaceLaneVecI16x8(void);
BinaryenOp BinaryenSplatVecI32x4(void);
BinaryenOp BinaryenExtractLaneVecI32x4(void);
BinaryenOp BinaryenReplaceLaneVecI32x4(void);
BinaryenOp BinaryenSplatVecI64x2(void);
BinaryenOp BinaryenExtractLaneVecI64x2(void);
BinaryenOp BinaryenReplaceLaneVecI64x2(void);
BinaryenOp BinaryenSplatVecF32x4(void);
BinaryenOp BinaryenExtractLaneVecF32x4(void);
BinaryenOp BinaryenReplaceLaneVecF32x4(void);
BinaryenOp BinaryenSplatVecF64x2(void);
BinaryenOp BinaryenExtractLaneVecF64x2(void);
BinaryenOp BinaryenReplaceLaneVecF64x2(void);
BinaryenOp BinaryenEqVecI8x16(void);
BinaryenOp BinaryenNeVecI8x16(void);
BinaryenOp BinaryenLtSVecI8x16(void);
BinaryenOp BinaryenLtUVecI8x16(void);
BinaryenOp BinaryenGtSVecI8x16(void);
BinaryenOp BinaryenGtUVecI8x16(void);
BinaryenOp BinaryenLeSVecI8x16(void);
BinaryenOp BinaryenLeUVecI8x16(void);
BinaryenOp BinaryenGeSVecI8x16(void);
BinaryenOp BinaryenGeUVecI8x16(void);
BinaryenOp BinaryenEqVecI16x8(void);
BinaryenOp BinaryenNeVecI16x8(void);
BinaryenOp BinaryenLtSVecI16x8(void);
BinaryenOp BinaryenLtUVecI16x8(void);
BinaryenOp BinaryenGtSVecI16x8(void);
BinaryenOp BinaryenGtUVecI16x8(void);
BinaryenOp BinaryenLeSVecI16x8(void);
BinaryenOp BinaryenLeUVecI16x8(void);
BinaryenOp BinaryenGeSVecI16x8(void);
BinaryenOp BinaryenGeUVecI16x8(void);
BinaryenOp BinaryenEqVecI32x4(void);
BinaryenOp BinaryenNeVecI32x4(void);
BinaryenOp BinaryenLtSVecI32x4(void);
BinaryenOp BinaryenLtUVecI32x4(void);
BinaryenOp BinaryenGtSVecI32x4(void);
BinaryenOp BinaryenGtUVecI32x4(void);
BinaryenOp BinaryenLeSVecI32x4(void);
BinaryenOp BinaryenLeUVecI32x4(void);
BinaryenOp BinaryenGeSVecI32x4(void);
BinaryenOp BinaryenGeUVecI32x4(void);
BinaryenOp BinaryenEqVecI64x2(void);
BinaryenOp BinaryenNeVecI64x2(void);
BinaryenOp BinaryenLtSVecI64x2(void);
BinaryenOp BinaryenGtSVecI64x2(void);
BinaryenOp BinaryenLeSVecI64x2(void);
BinaryenOp BinaryenGeSVecI64x2(void);
BinaryenOp BinaryenEqVecF32x4(void);
BinaryenOp BinaryenNeVecF32x4(void);
BinaryenOp BinaryenLtVecF32x4(void);
BinaryenOp BinaryenGtVecF32x4(void);
BinaryenOp BinaryenLeVecF32x4(void);
BinaryenOp BinaryenGeVecF32x4(void);
BinaryenOp BinaryenEqVecF64x2(void);
BinaryenOp BinaryenNeVecF64x2(void);
BinaryenOp BinaryenLtVecF64x2(void);
BinaryenOp BinaryenGtVecF64x2(void);
BinaryenOp BinaryenLeVecF64x2(void);
BinaryenOp BinaryenGeVecF64x2(void);
BinaryenOp BinaryenNotVec128(void);
BinaryenOp BinaryenAndVec128(void);
BinaryenOp BinaryenOrVec128(void);
BinaryenOp BinaryenXorVec128(void);
BinaryenOp BinaryenAndNotVec128(void);
BinaryenOp BinaryenBitselectVec128(void);
BinaryenOp BinaryenRelaxedFmaVecF32x4(void);
BinaryenOp BinaryenRelaxedFmsVecF32x4(void);
BinaryenOp BinaryenRelaxedFmaVecF64x2(void);
BinaryenOp BinaryenRelaxedFmsVecF64x2(void);
BinaryenOp BinaryenLaneselectI8x16(void);
BinaryenOp BinaryenLaneselectI16x8(void);
BinaryenOp BinaryenLaneselectI32x4(void);
BinaryenOp BinaryenLaneselectI64x2(void);
BinaryenOp BinaryenDotI8x16I7x16AddSToVecI32x4(void);
BinaryenOp BinaryenAnyTrueVec128(void);
BinaryenOp BinaryenPopcntVecI8x16(void);
BinaryenOp BinaryenAbsVecI8x16(void);
BinaryenOp BinaryenNegVecI8x16(void);
BinaryenOp BinaryenAllTrueVecI8x16(void);
BinaryenOp BinaryenBitmaskVecI8x16(void);
BinaryenOp BinaryenShlVecI8x16(void);
BinaryenOp BinaryenShrSVecI8x16(void);
BinaryenOp BinaryenShrUVecI8x16(void);
BinaryenOp BinaryenAddVecI8x16(void);
BinaryenOp BinaryenAddSatSVecI8x16(void);
BinaryenOp BinaryenAddSatUVecI8x16(void);
BinaryenOp BinaryenSubVecI8x16(void);
BinaryenOp BinaryenSubSatSVecI8x16(void);
BinaryenOp BinaryenSubSatUVecI8x16(void);
BinaryenOp BinaryenMinSVecI8x16(void);
BinaryenOp BinaryenMinUVecI8x16(void);
BinaryenOp BinaryenMaxSVecI8x16(void);
BinaryenOp BinaryenMaxUVecI8x16(void);
BinaryenOp BinaryenAvgrUVecI8x16(void);
BinaryenOp BinaryenAbsVecI16x8(void);
BinaryenOp BinaryenNegVecI16x8(void);
BinaryenOp BinaryenAllTrueVecI16x8(void);
BinaryenOp BinaryenBitmaskVecI16x8(void);
BinaryenOp BinaryenShlVecI16x8(void);
BinaryenOp BinaryenShrSVecI16x8(void);
BinaryenOp BinaryenShrUVecI16x8(void);
BinaryenOp BinaryenAddVecI16x8(void);
BinaryenOp BinaryenAddSatSVecI16x8(void);
BinaryenOp BinaryenAddSatUVecI16x8(void);
BinaryenOp BinaryenSubVecI16x8(void);
BinaryenOp BinaryenSubSatSVecI16x8(void);
BinaryenOp BinaryenSubSatUVecI16x8(void);
BinaryenOp BinaryenMulVecI16x8(void);
BinaryenOp BinaryenMinSVecI16x8(void);
BinaryenOp BinaryenMinUVecI16x8(void);
BinaryenOp BinaryenMaxSVecI16x8(void);
BinaryenOp BinaryenMaxUVecI16x8(void);
BinaryenOp BinaryenAvgrUVecI16x8(void);
BinaryenOp BinaryenQ15MulrSatSVecI16x8(void);
BinaryenOp BinaryenExtMulLowSVecI16x8(void);
BinaryenOp BinaryenExtMulHighSVecI16x8(void);
BinaryenOp BinaryenExtMulLowUVecI16x8(void);
BinaryenOp BinaryenExtMulHighUVecI16x8(void);
BinaryenOp BinaryenAbsVecI32x4(void);
BinaryenOp BinaryenNegVecI32x4(void);
BinaryenOp BinaryenAllTrueVecI32x4(void);
BinaryenOp BinaryenBitmaskVecI32x4(void);
BinaryenOp BinaryenShlVecI32x4(void);
BinaryenOp BinaryenShrSVecI32x4(void);
BinaryenOp BinaryenShrUVecI32x4(void);
BinaryenOp BinaryenAddVecI32x4(void);
BinaryenOp BinaryenSubVecI32x4(void);
BinaryenOp BinaryenMulVecI32x4(void);
BinaryenOp BinaryenMinSVecI32x4(void);
BinaryenOp BinaryenMinUVecI32x4(void);
BinaryenOp BinaryenMaxSVecI32x4(void);
BinaryenOp BinaryenMaxUVecI32x4(void);
BinaryenOp BinaryenDotSVecI16x8ToVecI32x4(void);
BinaryenOp BinaryenExtMulLowSVecI32x4(void);
BinaryenOp BinaryenExtMulHighSVecI32x4(void);
BinaryenOp BinaryenExtMulLowUVecI32x4(void);
BinaryenOp BinaryenExtMulHighUVecI32x4(void);
BinaryenOp BinaryenAbsVecI64x2(void);
BinaryenOp BinaryenNegVecI64x2(void);
BinaryenOp BinaryenAllTrueVecI64x2(void);
BinaryenOp BinaryenBitmaskVecI64x2(void);
BinaryenOp BinaryenShlVecI64x2(void);
BinaryenOp BinaryenShrSVecI64x2(void);
BinaryenOp BinaryenShrUVecI64x2(void);
BinaryenOp BinaryenAddVecI64x2(void);
BinaryenOp BinaryenSubVecI64x2(void);
BinaryenOp BinaryenMulVecI64x2(void);
BinaryenOp BinaryenExtMulLowSVecI64x2(void);
BinaryenOp BinaryenExtMulHighSVecI64x2(void);
BinaryenOp BinaryenExtMulLowUVecI64x2(void);
BinaryenOp BinaryenExtMulHighUVecI64x2(void);
BinaryenOp BinaryenAbsVecF32x4(void);
BinaryenOp BinaryenNegVecF32x4(void);
BinaryenOp BinaryenSqrtVecF32x4(void);
BinaryenOp BinaryenAddVecF32x4(void);
BinaryenOp BinaryenSubVecF32x4(void);
BinaryenOp BinaryenMulVecF32x4(void);
BinaryenOp BinaryenDivVecF32x4(void);
BinaryenOp BinaryenMinVecF32x4(void);
BinaryenOp BinaryenMaxVecF32x4(void);
BinaryenOp BinaryenPMinVecF32x4(void);
BinaryenOp BinaryenPMaxVecF32x4(void);
BinaryenOp BinaryenCeilVecF32x4(void);
BinaryenOp BinaryenFloorVecF32x4(void);
BinaryenOp BinaryenTruncVecF32x4(void);
BinaryenOp BinaryenNearestVecF32x4(void);
BinaryenOp BinaryenAbsVecF64x2(void);
BinaryenOp BinaryenNegVecF64x2(void);
BinaryenOp BinaryenSqrtVecF64x2(void);
BinaryenOp BinaryenAddVecF64x2(void);
BinaryenOp BinaryenSubVecF64x2(void);
BinaryenOp BinaryenMulVecF64x2(void);
BinaryenOp BinaryenDivVecF64x2(void);
BinaryenOp BinaryenMinVecF64x2(void);
BinaryenOp BinaryenMaxVecF64x2(void);
BinaryenOp BinaryenPMinVecF64x2(void);
BinaryenOp BinaryenPMaxVecF64x2(void);
BinaryenOp BinaryenCeilVecF64x2(void);
BinaryenOp BinaryenFloorVecF64x2(void);
BinaryenOp BinaryenTruncVecF64x2(void);
BinaryenOp BinaryenNearestVecF64x2(void);
BinaryenOp BinaryenExtAddPairwiseSVecI8x16ToI16x8(void);
BinaryenOp BinaryenExtAddPairwiseUVecI8x16ToI16x8(void);
BinaryenOp BinaryenExtAddPairwiseSVecI16x8ToI32x4(void);
BinaryenOp BinaryenExtAddPairwiseUVecI16x8ToI32x4(void);
BinaryenOp BinaryenTruncSatSVecF32x4ToVecI32x4(void);
BinaryenOp BinaryenTruncSatUVecF32x4ToVecI32x4(void);
BinaryenOp BinaryenConvertSVecI32x4ToVecF32x4(void);
BinaryenOp BinaryenConvertUVecI32x4ToVecF32x4(void);
BinaryenOp BinaryenLoad8SplatVec128(void);
BinaryenOp BinaryenLoad16SplatVec128(void);
BinaryenOp BinaryenLoad32SplatVec128(void);
BinaryenOp BinaryenLoad64SplatVec128(void);
BinaryenOp BinaryenLoad8x8SVec128(void);
BinaryenOp BinaryenLoad8x8UVec128(void);
BinaryenOp BinaryenLoad16x4SVec128(void);
BinaryenOp BinaryenLoad16x4UVec128(void);
BinaryenOp BinaryenLoad32x2SVec128(void);
BinaryenOp BinaryenLoad32x2UVec128(void);
BinaryenOp BinaryenLoad32ZeroVec128(void);
BinaryenOp BinaryenLoad64ZeroVec128(void);
BinaryenOp BinaryenLoad8LaneVec128(void);
BinaryenOp BinaryenLoad16LaneVec128(void);
BinaryenOp BinaryenLoad32LaneVec128(void);
BinaryenOp BinaryenLoad64LaneVec128(void);
BinaryenOp BinaryenStore8LaneVec128(void);
BinaryenOp BinaryenStore16LaneVec128(void);
BinaryenOp BinaryenStore32LaneVec128(void);
BinaryenOp BinaryenStore64LaneVec128(void);
BinaryenOp BinaryenNarrowSVecI16x8ToVecI8x16(void);
BinaryenOp BinaryenNarrowUVecI16x8ToVecI8x16(void);
BinaryenOp BinaryenNarrowSVecI32x4ToVecI16x8(void);
BinaryenOp BinaryenNarrowUVecI32x4ToVecI16x8(void);
BinaryenOp BinaryenExtendLowSVecI8x16ToVecI16x8(void);
BinaryenOp BinaryenExtendHighSVecI8x16ToVecI16x8(void);
BinaryenOp BinaryenExtendLowUVecI8x16ToVecI16x8(void);
BinaryenOp BinaryenExtendHighUVecI8x16ToVecI16x8(void);
BinaryenOp BinaryenExtendLowSVecI16x8ToVecI32x4(void);
BinaryenOp BinaryenExtendHighSVecI16x8ToVecI32x4(void);
BinaryenOp BinaryenExtendLowUVecI16x8ToVecI32x4(void);
BinaryenOp BinaryenExtendHighUVecI16x8ToVecI32x4(void);
BinaryenOp BinaryenExtendLowSVecI32x4ToVecI64x2(void);
BinaryenOp BinaryenExtendHighSVecI32x4ToVecI64x2(void);
BinaryenOp BinaryenExtendLowUVecI32x4ToVecI64x2(void);
BinaryenOp BinaryenExtendHighUVecI32x4ToVecI64x2(void);
BinaryenOp BinaryenConvertLowSVecI32x4ToVecF64x2(void);
BinaryenOp BinaryenConvertLowUVecI32x4ToVecF64x2(void);
BinaryenOp BinaryenTruncSatZeroSVecF64x2ToVecI32x4(void);
BinaryenOp BinaryenTruncSatZeroUVecF64x2ToVecI32x4(void);
BinaryenOp BinaryenDemoteZeroVecF64x2ToVecF32x4(void);
BinaryenOp BinaryenPromoteLowVecF32x4ToVecF64x2(void);
BinaryenOp BinaryenRelaxedTruncSVecF32x4ToVecI32x4(void);
BinaryenOp BinaryenRelaxedTruncUVecF32x4ToVecI32x4(void);
BinaryenOp BinaryenRelaxedTruncZeroSVecF64x2ToVecI32x4(void);
BinaryenOp BinaryenRelaxedTruncZeroUVecF64x2ToVecI32x4(void);
BinaryenOp BinaryenSwizzleVecI8x16(void);
BinaryenOp BinaryenRelaxedSwizzleVecI8x16(void);
BinaryenOp BinaryenRelaxedMinVecF32x4(void);
BinaryenOp BinaryenRelaxedMaxVecF32x4(void);
BinaryenOp BinaryenRelaxedMinVecF64x2(void);
BinaryenOp BinaryenRelaxedMaxVecF64x2(void);
BinaryenOp BinaryenRelaxedQ15MulrSVecI16x8(void);
BinaryenOp BinaryenDotI8x16I7x16SToVecI16x8(void);
BinaryenOp BinaryenRefAsNonNull(void);
BinaryenOp BinaryenRefAsExternInternalize(void);
BinaryenOp BinaryenRefAsExternExternalize(void);
BinaryenOp BinaryenBrOnNull(void);
BinaryenOp BinaryenBrOnNonNull(void);
BinaryenOp BinaryenBrOnCast(void);
BinaryenOp BinaryenBrOnCastFail(void);
BinaryenOp BinaryenStringNewUTF8(void);
BinaryenOp BinaryenStringNewWTF8(void);
BinaryenOp BinaryenStringNewLossyUTF8(void);
BinaryenOp BinaryenStringNewWTF16(void);
BinaryenOp BinaryenStringNewUTF8Array(void);
BinaryenOp BinaryenStringNewWTF8Array(void);
BinaryenOp BinaryenStringNewLossyUTF8Array(void);
BinaryenOp BinaryenStringNewWTF16Array(void);
BinaryenOp BinaryenStringNewFromCodePoint(void);
BinaryenOp BinaryenStringMeasureUTF8(void);
BinaryenOp BinaryenStringMeasureWTF8(void);
BinaryenOp BinaryenStringMeasureWTF16(void);
BinaryenOp BinaryenStringMeasureIsUSV(void);
BinaryenOp BinaryenStringMeasureWTF16View(void);
BinaryenOp BinaryenStringEncodeUTF8(void);
BinaryenOp BinaryenStringEncodeLossyUTF8(void);
BinaryenOp BinaryenStringEncodeWTF8(void);
BinaryenOp BinaryenStringEncodeWTF16(void);
BinaryenOp BinaryenStringEncodeUTF8Array(void);
BinaryenOp BinaryenStringEncodeLossyUTF8Array(void);
BinaryenOp BinaryenStringEncodeWTF8Array(void);
BinaryenOp BinaryenStringEncodeWTF16Array(void);
BinaryenOp BinaryenStringAsWTF8(void);
BinaryenOp BinaryenStringAsWTF16(void);
BinaryenOp BinaryenStringAsIter(void);
BinaryenOp BinaryenStringIterMoveAdvance(void);
BinaryenOp BinaryenStringIterMoveRewind(void);
BinaryenOp BinaryenStringSliceWTF8(void);
BinaryenOp BinaryenStringSliceWTF16(void);
BinaryenOp BinaryenStringEqEqual(void);
BinaryenOp BinaryenStringEqCompare(void);
typedef struct BinaryenExpression *BinaryenExpressionRef;
;
BinaryenExpressionRef
BinaryenBlock(BinaryenModuleRef module,
              const char *name,
              BinaryenExpressionRef *children,
              BinaryenIndex numChildren,
              BinaryenType type);
BinaryenExpressionRef BinaryenIf(BinaryenModuleRef module,
                                 BinaryenExpressionRef condition,
                                 BinaryenExpressionRef ifTrue,
                                 BinaryenExpressionRef ifFalse);
BinaryenExpressionRef BinaryenLoop(BinaryenModuleRef module,
                                   const char *in,
                                   BinaryenExpressionRef body);
BinaryenExpressionRef
BinaryenBreak(BinaryenModuleRef module,
              const char *name,
              BinaryenExpressionRef condition,
              BinaryenExpressionRef value);
BinaryenExpressionRef
BinaryenSwitch(BinaryenModuleRef module,
               const char **names,
               BinaryenIndex numNames,
               const char *defaultName,
               BinaryenExpressionRef condition,
               BinaryenExpressionRef value);
BinaryenExpressionRef BinaryenCall(BinaryenModuleRef module,
                                   const char *target,
                                   BinaryenExpressionRef *operands,
                                   BinaryenIndex numOperands,
                                   BinaryenType returnType);
BinaryenExpressionRef
BinaryenCallIndirect(BinaryenModuleRef module,
                     const char *table,
                     BinaryenExpressionRef target,
                     BinaryenExpressionRef *operands,
                     BinaryenIndex numOperands,
                     BinaryenType params,
                     BinaryenType results);
BinaryenExpressionRef
BinaryenReturnCall(BinaryenModuleRef module,
                   const char *target,
                   BinaryenExpressionRef *operands,
                   BinaryenIndex numOperands,
                   BinaryenType returnType);
BinaryenExpressionRef
BinaryenReturnCallIndirect(BinaryenModuleRef module,
                           const char *table,
                           BinaryenExpressionRef target,
                           BinaryenExpressionRef *operands,
                           BinaryenIndex numOperands,
                           BinaryenType params,
                           BinaryenType results);
BinaryenExpressionRef BinaryenLocalGet(BinaryenModuleRef module,
                                       BinaryenIndex index,
                                       BinaryenType type);
BinaryenExpressionRef BinaryenLocalSet(
    BinaryenModuleRef module, BinaryenIndex index, BinaryenExpressionRef value);
BinaryenExpressionRef BinaryenLocalTee(BinaryenModuleRef module,
                                       BinaryenIndex index,
                                       BinaryenExpressionRef value,
                                       BinaryenType type);
BinaryenExpressionRef BinaryenGlobalGet(BinaryenModuleRef module,
                                        const char *name,
                                        BinaryenType type);
BinaryenExpressionRef BinaryenGlobalSet(
    BinaryenModuleRef module, const char *name, BinaryenExpressionRef value);
BinaryenExpressionRef BinaryenLoad(BinaryenModuleRef module,
                                   uint32_t bytes,
                                   bool signed_,
                                   uint32_t offset,
                                   uint32_t align,
                                   BinaryenType type,
                                   BinaryenExpressionRef ptr,
                                   const char *memoryName);
BinaryenExpressionRef BinaryenStore(BinaryenModuleRef module,
                                    uint32_t bytes,
                                    uint32_t offset,
                                    uint32_t align,
                                    BinaryenExpressionRef ptr,
                                    BinaryenExpressionRef value,
                                    BinaryenType type,
                                    const char *memoryName);
BinaryenExpressionRef BinaryenConst(BinaryenModuleRef module,
                                    struct BinaryenLiteral value);
BinaryenExpressionRef BinaryenUnary(BinaryenModuleRef module,
                                    BinaryenOp op,
                                    BinaryenExpressionRef value);
BinaryenExpressionRef BinaryenBinary(BinaryenModuleRef module,
                                     BinaryenOp op,
                                     BinaryenExpressionRef left,
                                     BinaryenExpressionRef right);
BinaryenExpressionRef
BinaryenSelect(BinaryenModuleRef module,
               BinaryenExpressionRef condition,
               BinaryenExpressionRef ifTrue,
               BinaryenExpressionRef ifFalse,
               BinaryenType type);
BinaryenExpressionRef BinaryenDrop(BinaryenModuleRef module,
                                   BinaryenExpressionRef value);
BinaryenExpressionRef BinaryenReturn(BinaryenModuleRef module,
                                     BinaryenExpressionRef value);
BinaryenExpressionRef BinaryenMemorySize(BinaryenModuleRef module,
                                         const char *memoryName,
                                         bool memoryIs64);
BinaryenExpressionRef
BinaryenMemoryGrow(BinaryenModuleRef module,
                   BinaryenExpressionRef delta,
                   const char *memoryName,
                   bool memoryIs64);
BinaryenExpressionRef BinaryenNop(BinaryenModuleRef module);
BinaryenExpressionRef
BinaryenUnreachable(BinaryenModuleRef module);
BinaryenExpressionRef BinaryenAtomicLoad(BinaryenModuleRef module,
                                         uint32_t bytes,
                                         uint32_t offset,
                                         BinaryenType type,
                                         BinaryenExpressionRef ptr,
                                         const char *memoryName);
BinaryenExpressionRef
BinaryenAtomicStore(BinaryenModuleRef module,
                    uint32_t bytes,
                    uint32_t offset,
                    BinaryenExpressionRef ptr,
                    BinaryenExpressionRef value,
                    BinaryenType type,
                    const char *memoryName);
BinaryenExpressionRef
BinaryenAtomicRMW(BinaryenModuleRef module,
                  BinaryenOp op,
                  BinaryenIndex bytes,
                  BinaryenIndex offset,
                  BinaryenExpressionRef ptr,
                  BinaryenExpressionRef value,
                  BinaryenType type,
                  const char *memoryName);
BinaryenExpressionRef
BinaryenAtomicCmpxchg(BinaryenModuleRef module,
                      BinaryenIndex bytes,
                      BinaryenIndex offset,
                      BinaryenExpressionRef ptr,
                      BinaryenExpressionRef expected,
                      BinaryenExpressionRef replacement,
                      BinaryenType type,
                      const char *memoryName);
BinaryenExpressionRef
BinaryenAtomicWait(BinaryenModuleRef module,
                   BinaryenExpressionRef ptr,
                   BinaryenExpressionRef expected,
                   BinaryenExpressionRef timeout,
                   BinaryenType type,
                   const char *memoryName);
BinaryenExpressionRef
BinaryenAtomicNotify(BinaryenModuleRef module,
                     BinaryenExpressionRef ptr,
                     BinaryenExpressionRef notifyCount,
                     const char *memoryName);
BinaryenExpressionRef
BinaryenAtomicFence(BinaryenModuleRef module);
BinaryenExpressionRef
BinaryenSIMDExtract(BinaryenModuleRef module,
                    BinaryenOp op,
                    BinaryenExpressionRef vec,
                    uint8_t index);
BinaryenExpressionRef
BinaryenSIMDReplace(BinaryenModuleRef module,
                    BinaryenOp op,
                    BinaryenExpressionRef vec,
                    uint8_t index,
                    BinaryenExpressionRef value);
BinaryenExpressionRef
BinaryenSIMDShuffle(BinaryenModuleRef module,
                    BinaryenExpressionRef left,
                    BinaryenExpressionRef right,
                    const uint8_t mask[16]);
BinaryenExpressionRef BinaryenSIMDTernary(BinaryenModuleRef module,
                                          BinaryenOp op,
                                          BinaryenExpressionRef a,
                                          BinaryenExpressionRef b,
                                          BinaryenExpressionRef c);
BinaryenExpressionRef
BinaryenSIMDShift(BinaryenModuleRef module,
                  BinaryenOp op,
                  BinaryenExpressionRef vec,
                  BinaryenExpressionRef shift);
BinaryenExpressionRef BinaryenSIMDLoad(BinaryenModuleRef module,
                                       BinaryenOp op,
                                       uint32_t offset,
                                       uint32_t align,
                                       BinaryenExpressionRef ptr,
                                       const char *name);
BinaryenExpressionRef
BinaryenSIMDLoadStoreLane(BinaryenModuleRef module,
                          BinaryenOp op,
                          uint32_t offset,
                          uint32_t align,
                          uint8_t index,
                          BinaryenExpressionRef ptr,
                          BinaryenExpressionRef vec,
                          const char *memoryName);
BinaryenExpressionRef
BinaryenMemoryInit(BinaryenModuleRef module,
                   const char *segment,
                   BinaryenExpressionRef dest,
                   BinaryenExpressionRef offset,
                   BinaryenExpressionRef size,
                   const char *memoryName);
BinaryenExpressionRef BinaryenDataDrop(BinaryenModuleRef module,
                                       const char *segment);
BinaryenExpressionRef
BinaryenMemoryCopy(BinaryenModuleRef module,
                   BinaryenExpressionRef dest,
                   BinaryenExpressionRef source,
                   BinaryenExpressionRef size,
                   const char *destMemory,
                   const char *sourceMemory);
BinaryenExpressionRef
BinaryenMemoryFill(BinaryenModuleRef module,
                   BinaryenExpressionRef dest,
                   BinaryenExpressionRef value,
                   BinaryenExpressionRef size,
                   const char *memoryName);
BinaryenExpressionRef BinaryenRefNull(BinaryenModuleRef module,
                                      BinaryenType type);
BinaryenExpressionRef
BinaryenRefIsNull(BinaryenModuleRef module, BinaryenExpressionRef value);
BinaryenExpressionRef BinaryenRefAs(BinaryenModuleRef module,
                                    BinaryenOp op,
                                    BinaryenExpressionRef value);
BinaryenExpressionRef BinaryenRefFunc(BinaryenModuleRef module,
                                      const char *func,
                                      BinaryenType type);
BinaryenExpressionRef BinaryenRefEq(BinaryenModuleRef module,
                                    BinaryenExpressionRef left,
                                    BinaryenExpressionRef right);
BinaryenExpressionRef BinaryenTableGet(BinaryenModuleRef module,
                                       const char *name,
                                       BinaryenExpressionRef index,
                                       BinaryenType type);
BinaryenExpressionRef
BinaryenTableSet(BinaryenModuleRef module,
                 const char *name,
                 BinaryenExpressionRef index,
                 BinaryenExpressionRef value);
BinaryenExpressionRef BinaryenTableSize(BinaryenModuleRef module,
                                        const char *name);
BinaryenExpressionRef
BinaryenTableGrow(BinaryenModuleRef module,
                  const char *name,
                  BinaryenExpressionRef value,
                  BinaryenExpressionRef delta);
BinaryenExpressionRef
BinaryenTry(BinaryenModuleRef module,
            const char *name,
            BinaryenExpressionRef body,
            const char **catchTags,
            BinaryenIndex numCatchTags,
            BinaryenExpressionRef *catchBodies,
            BinaryenIndex numCatchBodies,
            const char *delegateTarget);
BinaryenExpressionRef
BinaryenThrow(BinaryenModuleRef module,
              const char *tag,
              BinaryenExpressionRef *operands,
              BinaryenIndex numOperands);
BinaryenExpressionRef BinaryenRethrow(BinaryenModuleRef module,
                                      const char *target);
BinaryenExpressionRef
BinaryenTupleMake(BinaryenModuleRef module,
                  BinaryenExpressionRef *operands,
                  BinaryenIndex numOperands);
BinaryenExpressionRef BinaryenTupleExtract(
    BinaryenModuleRef module, BinaryenExpressionRef tuple, BinaryenIndex index);
BinaryenExpressionRef BinaryenPop(BinaryenModuleRef module,
                                  BinaryenType type);
BinaryenExpressionRef BinaryenI31New(BinaryenModuleRef module,
                                     BinaryenExpressionRef value);
BinaryenExpressionRef BinaryenI31Get(BinaryenModuleRef module,
                                     BinaryenExpressionRef i31,
                                     bool signed_);
BinaryenExpressionRef
BinaryenCallRef(BinaryenModuleRef module,
                BinaryenExpressionRef target,
                BinaryenExpressionRef *operands,
                BinaryenIndex numOperands,
                BinaryenType type,
                bool isReturn);
BinaryenExpressionRef BinaryenRefTest(BinaryenModuleRef module,
                                      BinaryenExpressionRef ref,
                                      BinaryenType castType);
BinaryenExpressionRef BinaryenRefCast(BinaryenModuleRef module,
                                      BinaryenExpressionRef ref,
                                      BinaryenType type);
BinaryenExpressionRef BinaryenBrOn(BinaryenModuleRef module,
                                   BinaryenOp op,
                                   const char *name,
                                   BinaryenExpressionRef ref,
                                   BinaryenType castType);
BinaryenExpressionRef
BinaryenStructNew(BinaryenModuleRef module,
                  BinaryenExpressionRef *operands,
                  BinaryenIndex numOperands,
                  BinaryenHeapType type);
BinaryenExpressionRef BinaryenStructGet(BinaryenModuleRef module,
                                        BinaryenIndex index,
                                        BinaryenExpressionRef ref,
                                        BinaryenType type,
                                        bool signed_);
BinaryenExpressionRef
BinaryenStructSet(BinaryenModuleRef module,
                  BinaryenIndex index,
                  BinaryenExpressionRef ref,
                  BinaryenExpressionRef value);
BinaryenExpressionRef BinaryenArrayNew(BinaryenModuleRef module,
                                       BinaryenHeapType type,
                                       BinaryenExpressionRef size,
                                       BinaryenExpressionRef init);
BinaryenExpressionRef
BinaryenArrayNewFixed(BinaryenModuleRef module,
                      BinaryenHeapType type,
                      BinaryenExpressionRef *values,
                      BinaryenIndex numValues);
BinaryenExpressionRef BinaryenArrayGet(BinaryenModuleRef module,
                                       BinaryenExpressionRef ref,
                                       BinaryenExpressionRef index,
                                       BinaryenType type,
                                       bool signed_);
BinaryenExpressionRef
BinaryenArraySet(BinaryenModuleRef module,
                 BinaryenExpressionRef ref,
                 BinaryenExpressionRef index,
                 BinaryenExpressionRef value);
BinaryenExpressionRef BinaryenArrayLen(BinaryenModuleRef module,
                                       BinaryenExpressionRef ref);
BinaryenExpressionRef
BinaryenArrayCopy(BinaryenModuleRef module,
                  BinaryenExpressionRef destRef,
                  BinaryenExpressionRef destIndex,
                  BinaryenExpressionRef srcRef,
                  BinaryenExpressionRef srcIndex,
                  BinaryenExpressionRef length);
BinaryenExpressionRef
BinaryenStringNew(BinaryenModuleRef module,
                  BinaryenOp op,
                  BinaryenExpressionRef ptr,
                  BinaryenExpressionRef length,
                  BinaryenExpressionRef start,
                  BinaryenExpressionRef end,
                  bool try_);
BinaryenExpressionRef BinaryenStringConst(BinaryenModuleRef module,
                                          const char *name);
BinaryenExpressionRef BinaryenStringMeasure(
    BinaryenModuleRef module, BinaryenOp op, BinaryenExpressionRef ref);
BinaryenExpressionRef
BinaryenStringEncode(BinaryenModuleRef module,
                     BinaryenOp op,
                     BinaryenExpressionRef ref,
                     BinaryenExpressionRef ptr,
                     BinaryenExpressionRef start);
BinaryenExpressionRef
BinaryenStringConcat(BinaryenModuleRef module,
                     BinaryenExpressionRef left,
                     BinaryenExpressionRef right);
BinaryenExpressionRef
BinaryenStringEq(BinaryenModuleRef module,
                 BinaryenOp op,
                 BinaryenExpressionRef left,
                 BinaryenExpressionRef right);
BinaryenExpressionRef BinaryenStringAs(BinaryenModuleRef module,
                                       BinaryenOp op,
                                       BinaryenExpressionRef ref);
BinaryenExpressionRef
BinaryenStringWTF8Advance(BinaryenModuleRef module,
                          BinaryenExpressionRef ref,
                          BinaryenExpressionRef pos,
                          BinaryenExpressionRef bytes);
BinaryenExpressionRef
BinaryenStringWTF16Get(BinaryenModuleRef module,
                       BinaryenExpressionRef ref,
                       BinaryenExpressionRef pos);
BinaryenExpressionRef
BinaryenStringIterNext(BinaryenModuleRef module, BinaryenExpressionRef ref);
BinaryenExpressionRef
BinaryenStringIterMove(BinaryenModuleRef module,
                       BinaryenOp op,
                       BinaryenExpressionRef ref,
                       BinaryenExpressionRef num);
BinaryenExpressionRef
BinaryenStringSliceWTF(BinaryenModuleRef module,
                       BinaryenOp op,
                       BinaryenExpressionRef ref,
                       BinaryenExpressionRef start,
                       BinaryenExpressionRef end);
BinaryenExpressionRef
BinaryenStringSliceIter(BinaryenModuleRef module,
                        BinaryenExpressionRef ref,
                        BinaryenExpressionRef num);
BinaryenExpressionId
BinaryenExpressionGetId(BinaryenExpressionRef expr);
BinaryenType BinaryenExpressionGetType(BinaryenExpressionRef expr);
void BinaryenExpressionSetType(BinaryenExpressionRef expr,
                               BinaryenType type);
void BinaryenExpressionPrint(BinaryenExpressionRef expr);
void BinaryenExpressionFinalize(BinaryenExpressionRef expr);
BinaryenExpressionRef
BinaryenExpressionCopy(BinaryenExpressionRef expr, BinaryenModuleRef module);
const char *BinaryenBlockGetName(BinaryenExpressionRef expr);
void BinaryenBlockSetName(BinaryenExpressionRef expr,
                          const char *name);
BinaryenIndex
BinaryenBlockGetNumChildren(BinaryenExpressionRef expr);
BinaryenExpressionRef
BinaryenBlockGetChildAt(BinaryenExpressionRef expr, BinaryenIndex index);
void BinaryenBlockSetChildAt(BinaryenExpressionRef expr,
                             BinaryenIndex index,
                             BinaryenExpressionRef childExpr);
BinaryenIndex BinaryenBlockAppendChild(
    BinaryenExpressionRef expr, BinaryenExpressionRef childExpr);
void BinaryenBlockInsertChildAt(BinaryenExpressionRef expr,
                                BinaryenIndex index,
                                BinaryenExpressionRef childExpr);
BinaryenExpressionRef
BinaryenBlockRemoveChildAt(BinaryenExpressionRef expr, BinaryenIndex index);
BinaryenExpressionRef
BinaryenIfGetCondition(BinaryenExpressionRef expr);
void BinaryenIfSetCondition(BinaryenExpressionRef expr,
                            BinaryenExpressionRef condExpr);
BinaryenExpressionRef
BinaryenIfGetIfTrue(BinaryenExpressionRef expr);
void BinaryenIfSetIfTrue(BinaryenExpressionRef expr,
                         BinaryenExpressionRef ifTrueExpr);
BinaryenExpressionRef
BinaryenIfGetIfFalse(BinaryenExpressionRef expr);
void BinaryenIfSetIfFalse(BinaryenExpressionRef expr,
                          BinaryenExpressionRef ifFalseExpr);
const char *BinaryenLoopGetName(BinaryenExpressionRef expr);
void BinaryenLoopSetName(BinaryenExpressionRef expr,
                         const char *name);
BinaryenExpressionRef
BinaryenLoopGetBody(BinaryenExpressionRef expr);
void BinaryenLoopSetBody(BinaryenExpressionRef expr,
                         BinaryenExpressionRef bodyExpr);
const char *BinaryenBreakGetName(BinaryenExpressionRef expr);
void BinaryenBreakSetName(BinaryenExpressionRef expr,
                          const char *name);
BinaryenExpressionRef
BinaryenBreakGetCondition(BinaryenExpressionRef expr);
void BinaryenBreakSetCondition(BinaryenExpressionRef expr,
                               BinaryenExpressionRef condExpr);
BinaryenExpressionRef
BinaryenBreakGetValue(BinaryenExpressionRef expr);
void BinaryenBreakSetValue(BinaryenExpressionRef expr,
                           BinaryenExpressionRef valueExpr);
BinaryenIndex
BinaryenSwitchGetNumNames(BinaryenExpressionRef expr);
const char *BinaryenSwitchGetNameAt(BinaryenExpressionRef expr,
                                    BinaryenIndex index);
void BinaryenSwitchSetNameAt(BinaryenExpressionRef expr,
                             BinaryenIndex index,
                             const char *name);
BinaryenIndex BinaryenSwitchAppendName(BinaryenExpressionRef expr,
                                       const char *name);
void BinaryenSwitchInsertNameAt(BinaryenExpressionRef expr,
                                BinaryenIndex index,
                                const char *name);
const char *BinaryenSwitchRemoveNameAt(BinaryenExpressionRef expr,
                                       BinaryenIndex index);
const char *
BinaryenSwitchGetDefaultName(BinaryenExpressionRef expr);
void BinaryenSwitchSetDefaultName(BinaryenExpressionRef expr,
                                  const char *name);
BinaryenExpressionRef
BinaryenSwitchGetCondition(BinaryenExpressionRef expr);
void BinaryenSwitchSetCondition(BinaryenExpressionRef expr,
                                BinaryenExpressionRef condExpr);
BinaryenExpressionRef
BinaryenSwitchGetValue(BinaryenExpressionRef expr);
void BinaryenSwitchSetValue(BinaryenExpressionRef expr,
                            BinaryenExpressionRef valueExpr);
const char *BinaryenCallGetTarget(BinaryenExpressionRef expr);
void BinaryenCallSetTarget(BinaryenExpressionRef expr,
                           const char *target);
BinaryenIndex
BinaryenCallGetNumOperands(BinaryenExpressionRef expr);
BinaryenExpressionRef
BinaryenCallGetOperandAt(BinaryenExpressionRef expr, BinaryenIndex index);
void BinaryenCallSetOperandAt(BinaryenExpressionRef expr,
                              BinaryenIndex index,
                              BinaryenExpressionRef operandExpr);
BinaryenIndex BinaryenCallAppendOperand(
    BinaryenExpressionRef expr, BinaryenExpressionRef operandExpr);
void BinaryenCallInsertOperandAt(BinaryenExpressionRef expr,
                                 BinaryenIndex index,
                                 BinaryenExpressionRef operandExpr);
BinaryenExpressionRef
BinaryenCallRemoveOperandAt(BinaryenExpressionRef expr, BinaryenIndex index);
bool BinaryenCallIsReturn(BinaryenExpressionRef expr);
void BinaryenCallSetReturn(BinaryenExpressionRef expr,
                           bool isReturn);
BinaryenExpressionRef
BinaryenCallIndirectGetTarget(BinaryenExpressionRef expr);
void BinaryenCallIndirectSetTarget(BinaryenExpressionRef expr,
                                   BinaryenExpressionRef targetExpr);
const char *
BinaryenCallIndirectGetTable(BinaryenExpressionRef expr);
void BinaryenCallIndirectSetTable(BinaryenExpressionRef expr,
                                  const char *table);
BinaryenIndex
BinaryenCallIndirectGetNumOperands(BinaryenExpressionRef expr);
BinaryenExpressionRef BinaryenCallIndirectGetOperandAt(
    BinaryenExpressionRef expr, BinaryenIndex index);
void BinaryenCallIndirectSetOperandAt(BinaryenExpressionRef expr,
                                      BinaryenIndex index,
                                      BinaryenExpressionRef operandExpr);
BinaryenIndex BinaryenCallIndirectAppendOperand(
    BinaryenExpressionRef expr, BinaryenExpressionRef operandExpr);
void BinaryenCallIndirectInsertOperandAt(BinaryenExpressionRef expr,
                                         BinaryenIndex index,
                                         BinaryenExpressionRef operandExpr);
BinaryenExpressionRef BinaryenCallIndirectRemoveOperandAt(
    BinaryenExpressionRef expr, BinaryenIndex index);
bool BinaryenCallIndirectIsReturn(BinaryenExpressionRef expr);
void BinaryenCallIndirectSetReturn(BinaryenExpressionRef expr,
                                   bool isReturn);
BinaryenType
BinaryenCallIndirectGetParams(BinaryenExpressionRef expr);
void BinaryenCallIndirectSetParams(BinaryenExpressionRef expr,
                                   BinaryenType params);
BinaryenType
BinaryenCallIndirectGetResults(BinaryenExpressionRef expr);
void BinaryenCallIndirectSetResults(BinaryenExpressionRef expr,
                                    BinaryenType params);
BinaryenIndex BinaryenLocalGetGetIndex(BinaryenExpressionRef expr);
void BinaryenLocalGetSetIndex(BinaryenExpressionRef expr,
                              BinaryenIndex index);
bool BinaryenLocalSetIsTee(BinaryenExpressionRef expr);
BinaryenIndex BinaryenLocalSetGetIndex(BinaryenExpressionRef expr);
void BinaryenLocalSetSetIndex(BinaryenExpressionRef expr,
                              BinaryenIndex index);
BinaryenExpressionRef
BinaryenLocalSetGetValue(BinaryenExpressionRef expr);
void BinaryenLocalSetSetValue(BinaryenExpressionRef expr,
                              BinaryenExpressionRef valueExpr);
const char *BinaryenGlobalGetGetName(BinaryenExpressionRef expr);
void BinaryenGlobalGetSetName(BinaryenExpressionRef expr,
                              const char *name);
const char *BinaryenGlobalSetGetName(BinaryenExpressionRef expr);
void BinaryenGlobalSetSetName(BinaryenExpressionRef expr,
                              const char *name);
BinaryenExpressionRef
BinaryenGlobalSetGetValue(BinaryenExpressionRef expr);
void BinaryenGlobalSetSetValue(BinaryenExpressionRef expr,
                               BinaryenExpressionRef valueExpr);
const char *BinaryenTableGetGetTable(BinaryenExpressionRef expr);
void BinaryenTableGetSetTable(BinaryenExpressionRef expr,
                              const char *table);
BinaryenExpressionRef
BinaryenTableGetGetIndex(BinaryenExpressionRef expr);
void BinaryenTableGetSetIndex(BinaryenExpressionRef expr,
                              BinaryenExpressionRef indexExpr);
const char *BinaryenTableSetGetTable(BinaryenExpressionRef expr);
void BinaryenTableSetSetTable(BinaryenExpressionRef expr,
                              const char *table);
BinaryenExpressionRef
BinaryenTableSetGetIndex(BinaryenExpressionRef expr);
void BinaryenTableSetSetIndex(BinaryenExpressionRef expr,
                              BinaryenExpressionRef indexExpr);
BinaryenExpressionRef
BinaryenTableSetGetValue(BinaryenExpressionRef expr);
void BinaryenTableSetSetValue(BinaryenExpressionRef expr,
                              BinaryenExpressionRef valueExpr);
const char *BinaryenTableSizeGetTable(BinaryenExpressionRef expr);
void BinaryenTableSizeSetTable(BinaryenExpressionRef expr,
                               const char *table);
const char *BinaryenTableGrowGetTable(BinaryenExpressionRef expr);
void BinaryenTableGrowSetTable(BinaryenExpressionRef expr,
                               const char *table);
BinaryenExpressionRef
BinaryenTableGrowGetValue(BinaryenExpressionRef expr);
void BinaryenTableGrowSetValue(BinaryenExpressionRef expr,
                               BinaryenExpressionRef valueExpr);
BinaryenExpressionRef
BinaryenTableGrowGetDelta(BinaryenExpressionRef expr);
void BinaryenTableGrowSetDelta(BinaryenExpressionRef expr,
                               BinaryenExpressionRef deltaExpr);
BinaryenExpressionRef
BinaryenMemoryGrowGetDelta(BinaryenExpressionRef expr);
void BinaryenMemoryGrowSetDelta(BinaryenExpressionRef expr,
                                BinaryenExpressionRef deltaExpr);
bool BinaryenLoadIsAtomic(BinaryenExpressionRef expr);
void BinaryenLoadSetAtomic(BinaryenExpressionRef expr,
                           bool isAtomic);
bool BinaryenLoadIsSigned(BinaryenExpressionRef expr);
void BinaryenLoadSetSigned(BinaryenExpressionRef expr,
                           bool isSigned);
uint32_t BinaryenLoadGetOffset(BinaryenExpressionRef expr);
void BinaryenLoadSetOffset(BinaryenExpressionRef expr,
                           uint32_t offset);
uint32_t BinaryenLoadGetBytes(BinaryenExpressionRef expr);
void BinaryenLoadSetBytes(BinaryenExpressionRef expr,
                          uint32_t bytes);
uint32_t BinaryenLoadGetAlign(BinaryenExpressionRef expr);
void BinaryenLoadSetAlign(BinaryenExpressionRef expr,
                          uint32_t align);
BinaryenExpressionRef
BinaryenLoadGetPtr(BinaryenExpressionRef expr);
void BinaryenLoadSetPtr(BinaryenExpressionRef expr,
                        BinaryenExpressionRef ptrExpr);
bool BinaryenStoreIsAtomic(BinaryenExpressionRef expr);
void BinaryenStoreSetAtomic(BinaryenExpressionRef expr,
                            bool isAtomic);
uint32_t BinaryenStoreGetBytes(BinaryenExpressionRef expr);
void BinaryenStoreSetBytes(BinaryenExpressionRef expr,
                           uint32_t bytes);
uint32_t BinaryenStoreGetOffset(BinaryenExpressionRef expr);
void BinaryenStoreSetOffset(BinaryenExpressionRef expr,
                            uint32_t offset);
uint32_t BinaryenStoreGetAlign(BinaryenExpressionRef expr);
void BinaryenStoreSetAlign(BinaryenExpressionRef expr,
                           uint32_t align);
BinaryenExpressionRef
BinaryenStoreGetPtr(BinaryenExpressionRef expr);
void BinaryenStoreSetPtr(BinaryenExpressionRef expr,
                         BinaryenExpressionRef ptrExpr);
BinaryenExpressionRef
BinaryenStoreGetValue(BinaryenExpressionRef expr);
void BinaryenStoreSetValue(BinaryenExpressionRef expr,
                           BinaryenExpressionRef valueExpr);
BinaryenType BinaryenStoreGetValueType(BinaryenExpressionRef expr);
void BinaryenStoreSetValueType(BinaryenExpressionRef expr,
                               BinaryenType valueType);
int32_t BinaryenConstGetValueI32(BinaryenExpressionRef expr);
void BinaryenConstSetValueI32(BinaryenExpressionRef expr,
                              int32_t value);
int64_t BinaryenConstGetValueI64(BinaryenExpressionRef expr);
void BinaryenConstSetValueI64(BinaryenExpressionRef expr,
                              int64_t value);
int32_t BinaryenConstGetValueI64Low(BinaryenExpressionRef expr);
void BinaryenConstSetValueI64Low(BinaryenExpressionRef expr,
                                 int32_t valueLow);
int32_t BinaryenConstGetValueI64High(BinaryenExpressionRef expr);
void BinaryenConstSetValueI64High(BinaryenExpressionRef expr,
                                  int32_t valueHigh);
float BinaryenConstGetValueF32(BinaryenExpressionRef expr);
void BinaryenConstSetValueF32(BinaryenExpressionRef expr,
                              float value);
double BinaryenConstGetValueF64(BinaryenExpressionRef expr);
void BinaryenConstSetValueF64(BinaryenExpressionRef expr,
                              double value);
void BinaryenConstGetValueV128(BinaryenExpressionRef expr,
                               uint8_t *out);
void BinaryenConstSetValueV128(BinaryenExpressionRef expr,
                               const uint8_t value[16]);
BinaryenOp BinaryenUnaryGetOp(BinaryenExpressionRef expr);
void BinaryenUnarySetOp(BinaryenExpressionRef expr, BinaryenOp op);
BinaryenExpressionRef
BinaryenUnaryGetValue(BinaryenExpressionRef expr);
void BinaryenUnarySetValue(BinaryenExpressionRef expr,
                           BinaryenExpressionRef valueExpr);
BinaryenOp BinaryenBinaryGetOp(BinaryenExpressionRef expr);
void BinaryenBinarySetOp(BinaryenExpressionRef expr,
                         BinaryenOp op);
BinaryenExpressionRef
BinaryenBinaryGetLeft(BinaryenExpressionRef expr);
void BinaryenBinarySetLeft(BinaryenExpressionRef expr,
                           BinaryenExpressionRef leftExpr);
BinaryenExpressionRef
BinaryenBinaryGetRight(BinaryenExpressionRef expr);
void BinaryenBinarySetRight(BinaryenExpressionRef expr,
                            BinaryenExpressionRef rightExpr);
BinaryenExpressionRef
BinaryenSelectGetIfTrue(BinaryenExpressionRef expr);
void BinaryenSelectSetIfTrue(BinaryenExpressionRef expr,
                             BinaryenExpressionRef ifTrueExpr);
BinaryenExpressionRef
BinaryenSelectGetIfFalse(BinaryenExpressionRef expr);
void BinaryenSelectSetIfFalse(BinaryenExpressionRef expr,
                              BinaryenExpressionRef ifFalseExpr);
BinaryenExpressionRef
BinaryenSelectGetCondition(BinaryenExpressionRef expr);
void BinaryenSelectSetCondition(BinaryenExpressionRef expr,
                                BinaryenExpressionRef condExpr);
BinaryenExpressionRef
BinaryenDropGetValue(BinaryenExpressionRef expr);
void BinaryenDropSetValue(BinaryenExpressionRef expr,
                          BinaryenExpressionRef valueExpr);
BinaryenExpressionRef
BinaryenReturnGetValue(BinaryenExpressionRef expr);
void BinaryenReturnSetValue(BinaryenExpressionRef expr,
                            BinaryenExpressionRef valueExpr);
BinaryenOp BinaryenAtomicRMWGetOp(BinaryenExpressionRef expr);
void BinaryenAtomicRMWSetOp(BinaryenExpressionRef expr,
                            BinaryenOp op);
uint32_t BinaryenAtomicRMWGetBytes(BinaryenExpressionRef expr);
void BinaryenAtomicRMWSetBytes(BinaryenExpressionRef expr,
                               uint32_t bytes);
uint32_t BinaryenAtomicRMWGetOffset(BinaryenExpressionRef expr);
void BinaryenAtomicRMWSetOffset(BinaryenExpressionRef expr,
                                uint32_t offset);
BinaryenExpressionRef
BinaryenAtomicRMWGetPtr(BinaryenExpressionRef expr);
void BinaryenAtomicRMWSetPtr(BinaryenExpressionRef expr,
                             BinaryenExpressionRef ptrExpr);
BinaryenExpressionRef
BinaryenAtomicRMWGetValue(BinaryenExpressionRef expr);
void BinaryenAtomicRMWSetValue(BinaryenExpressionRef expr,
                               BinaryenExpressionRef valueExpr);
uint32_t BinaryenAtomicCmpxchgGetBytes(BinaryenExpressionRef expr);
void BinaryenAtomicCmpxchgSetBytes(BinaryenExpressionRef expr,
                                   uint32_t bytes);
uint32_t
BinaryenAtomicCmpxchgGetOffset(BinaryenExpressionRef expr);
void BinaryenAtomicCmpxchgSetOffset(BinaryenExpressionRef expr,
                                    uint32_t offset);
BinaryenExpressionRef
BinaryenAtomicCmpxchgGetPtr(BinaryenExpressionRef expr);
void BinaryenAtomicCmpxchgSetPtr(BinaryenExpressionRef expr,
                                 BinaryenExpressionRef ptrExpr);
BinaryenExpressionRef
BinaryenAtomicCmpxchgGetExpected(BinaryenExpressionRef expr);
void BinaryenAtomicCmpxchgSetExpected(BinaryenExpressionRef expr,
                                      BinaryenExpressionRef expectedExpr);
BinaryenExpressionRef
BinaryenAtomicCmpxchgGetReplacement(BinaryenExpressionRef expr);
void BinaryenAtomicCmpxchgSetReplacement(BinaryenExpressionRef expr,
                                         BinaryenExpressionRef replacementExpr);
BinaryenExpressionRef
BinaryenAtomicWaitGetPtr(BinaryenExpressionRef expr);
void BinaryenAtomicWaitSetPtr(BinaryenExpressionRef expr,
                              BinaryenExpressionRef ptrExpr);
BinaryenExpressionRef
BinaryenAtomicWaitGetExpected(BinaryenExpressionRef expr);
void BinaryenAtomicWaitSetExpected(BinaryenExpressionRef expr,
                                   BinaryenExpressionRef expectedExpr);
BinaryenExpressionRef
BinaryenAtomicWaitGetTimeout(BinaryenExpressionRef expr);
void BinaryenAtomicWaitSetTimeout(BinaryenExpressionRef expr,
                                  BinaryenExpressionRef timeoutExpr);
BinaryenType
BinaryenAtomicWaitGetExpectedType(BinaryenExpressionRef expr);
void BinaryenAtomicWaitSetExpectedType(BinaryenExpressionRef expr,
                                       BinaryenType expectedType);
BinaryenExpressionRef
BinaryenAtomicNotifyGetPtr(BinaryenExpressionRef expr);
void BinaryenAtomicNotifySetPtr(BinaryenExpressionRef expr,
                                BinaryenExpressionRef ptrExpr);
BinaryenExpressionRef
BinaryenAtomicNotifyGetNotifyCount(BinaryenExpressionRef expr);
void BinaryenAtomicNotifySetNotifyCount(BinaryenExpressionRef expr,
                                        BinaryenExpressionRef notifyCountExpr);
uint8_t BinaryenAtomicFenceGetOrder(BinaryenExpressionRef expr);
void BinaryenAtomicFenceSetOrder(BinaryenExpressionRef expr,
                                 uint8_t order);
BinaryenOp BinaryenSIMDExtractGetOp(BinaryenExpressionRef expr);
void BinaryenSIMDExtractSetOp(BinaryenExpressionRef expr,
                              BinaryenOp op);
BinaryenExpressionRef
BinaryenSIMDExtractGetVec(BinaryenExpressionRef expr);
void BinaryenSIMDExtractSetVec(BinaryenExpressionRef expr,
                               BinaryenExpressionRef vecExpr);
uint8_t BinaryenSIMDExtractGetIndex(BinaryenExpressionRef expr);
void BinaryenSIMDExtractSetIndex(BinaryenExpressionRef expr,
                                 uint8_t index);
BinaryenOp BinaryenSIMDReplaceGetOp(BinaryenExpressionRef expr);
void BinaryenSIMDReplaceSetOp(BinaryenExpressionRef expr,
                              BinaryenOp op);
BinaryenExpressionRef
BinaryenSIMDReplaceGetVec(BinaryenExpressionRef expr);
void BinaryenSIMDReplaceSetVec(BinaryenExpressionRef expr,
                               BinaryenExpressionRef vecExpr);
uint8_t BinaryenSIMDReplaceGetIndex(BinaryenExpressionRef expr);
void BinaryenSIMDReplaceSetIndex(BinaryenExpressionRef expr,
                                 uint8_t index);
BinaryenExpressionRef
BinaryenSIMDReplaceGetValue(BinaryenExpressionRef expr);
void BinaryenSIMDReplaceSetValue(BinaryenExpressionRef expr,
                                 BinaryenExpressionRef valueExpr);
BinaryenExpressionRef
BinaryenSIMDShuffleGetLeft(BinaryenExpressionRef expr);
void BinaryenSIMDShuffleSetLeft(BinaryenExpressionRef expr,
                                BinaryenExpressionRef leftExpr);
BinaryenExpressionRef
BinaryenSIMDShuffleGetRight(BinaryenExpressionRef expr);
void BinaryenSIMDShuffleSetRight(BinaryenExpressionRef expr,
                                 BinaryenExpressionRef rightExpr);
void BinaryenSIMDShuffleGetMask(BinaryenExpressionRef expr,
                                uint8_t *mask);
void BinaryenSIMDShuffleSetMask(BinaryenExpressionRef expr,
                                const uint8_t mask[16]);
BinaryenOp BinaryenSIMDTernaryGetOp(BinaryenExpressionRef expr);
void BinaryenSIMDTernarySetOp(BinaryenExpressionRef expr,
                              BinaryenOp op);
BinaryenExpressionRef
BinaryenSIMDTernaryGetA(BinaryenExpressionRef expr);
void BinaryenSIMDTernarySetA(BinaryenExpressionRef expr,
                             BinaryenExpressionRef aExpr);
BinaryenExpressionRef
BinaryenSIMDTernaryGetB(BinaryenExpressionRef expr);
void BinaryenSIMDTernarySetB(BinaryenExpressionRef expr,
                             BinaryenExpressionRef bExpr);
BinaryenExpressionRef
BinaryenSIMDTernaryGetC(BinaryenExpressionRef expr);
void BinaryenSIMDTernarySetC(BinaryenExpressionRef expr,
                             BinaryenExpressionRef cExpr);
BinaryenOp BinaryenSIMDShiftGetOp(BinaryenExpressionRef expr);
void BinaryenSIMDShiftSetOp(BinaryenExpressionRef expr,
                            BinaryenOp op);
BinaryenExpressionRef
BinaryenSIMDShiftGetVec(BinaryenExpressionRef expr);
void BinaryenSIMDShiftSetVec(BinaryenExpressionRef expr,
                             BinaryenExpressionRef vecExpr);
BinaryenExpressionRef
BinaryenSIMDShiftGetShift(BinaryenExpressionRef expr);
void BinaryenSIMDShiftSetShift(BinaryenExpressionRef expr,
                               BinaryenExpressionRef shiftExpr);
BinaryenOp BinaryenSIMDLoadGetOp(BinaryenExpressionRef expr);
void BinaryenSIMDLoadSetOp(BinaryenExpressionRef expr,
                           BinaryenOp op);
uint32_t BinaryenSIMDLoadGetOffset(BinaryenExpressionRef expr);
void BinaryenSIMDLoadSetOffset(BinaryenExpressionRef expr,
                               uint32_t offset);
uint32_t BinaryenSIMDLoadGetAlign(BinaryenExpressionRef expr);
void BinaryenSIMDLoadSetAlign(BinaryenExpressionRef expr,
                              uint32_t align);
BinaryenExpressionRef
BinaryenSIMDLoadGetPtr(BinaryenExpressionRef expr);
void BinaryenSIMDLoadSetPtr(BinaryenExpressionRef expr,
                            BinaryenExpressionRef ptrExpr);
BinaryenOp
BinaryenSIMDLoadStoreLaneGetOp(BinaryenExpressionRef expr);
void BinaryenSIMDLoadStoreLaneSetOp(BinaryenExpressionRef expr,
                                    BinaryenOp op);
uint32_t
BinaryenSIMDLoadStoreLaneGetOffset(BinaryenExpressionRef expr);
void BinaryenSIMDLoadStoreLaneSetOffset(BinaryenExpressionRef expr,
                                        uint32_t offset);
uint32_t
BinaryenSIMDLoadStoreLaneGetAlign(BinaryenExpressionRef expr);
void BinaryenSIMDLoadStoreLaneSetAlign(BinaryenExpressionRef expr,
                                       uint32_t align);
uint8_t
BinaryenSIMDLoadStoreLaneGetIndex(BinaryenExpressionRef expr);
void BinaryenSIMDLoadStoreLaneSetIndex(BinaryenExpressionRef expr,
                                       uint8_t index);
BinaryenExpressionRef
BinaryenSIMDLoadStoreLaneGetPtr(BinaryenExpressionRef expr);
void BinaryenSIMDLoadStoreLaneSetPtr(BinaryenExpressionRef expr,
                                     BinaryenExpressionRef ptrExpr);
BinaryenExpressionRef
BinaryenSIMDLoadStoreLaneGetVec(BinaryenExpressionRef expr);
void BinaryenSIMDLoadStoreLaneSetVec(BinaryenExpressionRef expr,
                                     BinaryenExpressionRef vecExpr);
bool BinaryenSIMDLoadStoreLaneIsStore(BinaryenExpressionRef expr);
const char *
BinaryenMemoryInitGetSegment(BinaryenExpressionRef expr);
void BinaryenMemoryInitSetSegment(BinaryenExpressionRef expr,
                                  const char *segment);
BinaryenExpressionRef
BinaryenMemoryInitGetDest(BinaryenExpressionRef expr);
void BinaryenMemoryInitSetDest(BinaryenExpressionRef expr,
                               BinaryenExpressionRef destExpr);
BinaryenExpressionRef
BinaryenMemoryInitGetOffset(BinaryenExpressionRef expr);
void BinaryenMemoryInitSetOffset(BinaryenExpressionRef expr,
                                 BinaryenExpressionRef offsetExpr);
BinaryenExpressionRef
BinaryenMemoryInitGetSize(BinaryenExpressionRef expr);
void BinaryenMemoryInitSetSize(BinaryenExpressionRef expr,
                               BinaryenExpressionRef sizeExpr);
const char *BinaryenDataDropGetSegment(BinaryenExpressionRef expr);
void BinaryenDataDropSetSegment(BinaryenExpressionRef expr,
                                const char *segment);
BinaryenExpressionRef
BinaryenMemoryCopyGetDest(BinaryenExpressionRef expr);
void BinaryenMemoryCopySetDest(BinaryenExpressionRef expr,
                               BinaryenExpressionRef destExpr);
BinaryenExpressionRef
BinaryenMemoryCopyGetSource(BinaryenExpressionRef expr);
void BinaryenMemoryCopySetSource(BinaryenExpressionRef expr,
                                 BinaryenExpressionRef sourceExpr);
BinaryenExpressionRef
BinaryenMemoryCopyGetSize(BinaryenExpressionRef expr);
void BinaryenMemoryCopySetSize(BinaryenExpressionRef expr,
                               BinaryenExpressionRef sizeExpr);
BinaryenExpressionRef
BinaryenMemoryFillGetDest(BinaryenExpressionRef expr);
void BinaryenMemoryFillSetDest(BinaryenExpressionRef expr,
                               BinaryenExpressionRef destExpr);
BinaryenExpressionRef
BinaryenMemoryFillGetValue(BinaryenExpressionRef expr);
void BinaryenMemoryFillSetValue(BinaryenExpressionRef expr,
                                BinaryenExpressionRef valueExpr);
BinaryenExpressionRef
BinaryenMemoryFillGetSize(BinaryenExpressionRef expr);
void BinaryenMemoryFillSetSize(BinaryenExpressionRef expr,
                               BinaryenExpressionRef sizeExpr);
BinaryenExpressionRef
BinaryenRefIsNullGetValue(BinaryenExpressionRef expr);
void BinaryenRefIsNullSetValue(BinaryenExpressionRef expr,
                               BinaryenExpressionRef valueExpr);
BinaryenOp BinaryenRefAsGetOp(BinaryenExpressionRef expr);
void BinaryenRefAsSetOp(BinaryenExpressionRef expr, BinaryenOp op);
BinaryenExpressionRef
BinaryenRefAsGetValue(BinaryenExpressionRef expr);
void BinaryenRefAsSetValue(BinaryenExpressionRef expr,
                           BinaryenExpressionRef valueExpr);
const char *BinaryenRefFuncGetFunc(BinaryenExpressionRef expr);
void BinaryenRefFuncSetFunc(BinaryenExpressionRef expr,
                            const char *funcName);
BinaryenExpressionRef
BinaryenRefEqGetLeft(BinaryenExpressionRef expr);
void BinaryenRefEqSetLeft(BinaryenExpressionRef expr,
                          BinaryenExpressionRef left);
BinaryenExpressionRef
BinaryenRefEqGetRight(BinaryenExpressionRef expr);
void BinaryenRefEqSetRight(BinaryenExpressionRef expr,
                           BinaryenExpressionRef right);
const char *BinaryenTryGetName(BinaryenExpressionRef expr);
void BinaryenTrySetName(BinaryenExpressionRef expr,
                        const char *name);
BinaryenExpressionRef
BinaryenTryGetBody(BinaryenExpressionRef expr);
void BinaryenTrySetBody(BinaryenExpressionRef expr,
                        BinaryenExpressionRef bodyExpr);
BinaryenIndex
BinaryenTryGetNumCatchTags(BinaryenExpressionRef expr);
BinaryenIndex
BinaryenTryGetNumCatchBodies(BinaryenExpressionRef expr);
const char *BinaryenTryGetCatchTagAt(BinaryenExpressionRef expr,
                                     BinaryenIndex index);
void BinaryenTrySetCatchTagAt(BinaryenExpressionRef expr,
                              BinaryenIndex index,
                              const char *catchTag);
BinaryenIndex BinaryenTryAppendCatchTag(BinaryenExpressionRef expr,
                                        const char *catchTag);
void BinaryenTryInsertCatchTagAt(BinaryenExpressionRef expr,
                                 BinaryenIndex index,
                                 const char *catchTag);
const char *BinaryenTryRemoveCatchTagAt(BinaryenExpressionRef expr,
                                        BinaryenIndex index);
BinaryenExpressionRef
BinaryenTryGetCatchBodyAt(BinaryenExpressionRef expr, BinaryenIndex index);
void BinaryenTrySetCatchBodyAt(BinaryenExpressionRef expr,
                               BinaryenIndex index,
                               BinaryenExpressionRef catchExpr);
BinaryenIndex BinaryenTryAppendCatchBody(
    BinaryenExpressionRef expr, BinaryenExpressionRef catchExpr);
void BinaryenTryInsertCatchBodyAt(BinaryenExpressionRef expr,
                                  BinaryenIndex index,
                                  BinaryenExpressionRef catchExpr);
BinaryenExpressionRef
BinaryenTryRemoveCatchBodyAt(BinaryenExpressionRef expr, BinaryenIndex index);
bool BinaryenTryHasCatchAll(BinaryenExpressionRef expr);
const char *
BinaryenTryGetDelegateTarget(BinaryenExpressionRef expr);
void BinaryenTrySetDelegateTarget(BinaryenExpressionRef expr,
                                  const char *delegateTarget);
bool BinaryenTryIsDelegate(BinaryenExpressionRef expr);
const char *BinaryenThrowGetTag(BinaryenExpressionRef expr);
void BinaryenThrowSetTag(BinaryenExpressionRef expr,
                         const char *tagName);
BinaryenIndex
BinaryenThrowGetNumOperands(BinaryenExpressionRef expr);
BinaryenExpressionRef
BinaryenThrowGetOperandAt(BinaryenExpressionRef expr, BinaryenIndex index);
void BinaryenThrowSetOperandAt(BinaryenExpressionRef expr,
                               BinaryenIndex index,
                               BinaryenExpressionRef operandExpr);
BinaryenIndex BinaryenThrowAppendOperand(
    BinaryenExpressionRef expr, BinaryenExpressionRef operandExpr);
void BinaryenThrowInsertOperandAt(BinaryenExpressionRef expr,
                                  BinaryenIndex index,
                                  BinaryenExpressionRef operandExpr);
BinaryenExpressionRef
BinaryenThrowRemoveOperandAt(BinaryenExpressionRef expr, BinaryenIndex index);
const char *BinaryenRethrowGetTarget(BinaryenExpressionRef expr);
void BinaryenRethrowSetTarget(BinaryenExpressionRef expr,
                              const char *target);
BinaryenIndex
BinaryenTupleMakeGetNumOperands(BinaryenExpressionRef expr);
BinaryenExpressionRef
BinaryenTupleMakeGetOperandAt(BinaryenExpressionRef expr, BinaryenIndex index);
void BinaryenTupleMakeSetOperandAt(BinaryenExpressionRef expr,
                                   BinaryenIndex index,
                                   BinaryenExpressionRef operandExpr);
BinaryenIndex BinaryenTupleMakeAppendOperand(
    BinaryenExpressionRef expr, BinaryenExpressionRef operandExpr);
void BinaryenTupleMakeInsertOperandAt(BinaryenExpressionRef expr,
                                      BinaryenIndex index,
                                      BinaryenExpressionRef operandExpr);
BinaryenExpressionRef BinaryenTupleMakeRemoveOperandAt(
    BinaryenExpressionRef expr, BinaryenIndex index);
BinaryenExpressionRef
BinaryenTupleExtractGetTuple(BinaryenExpressionRef expr);
void BinaryenTupleExtractSetTuple(BinaryenExpressionRef expr,
                                  BinaryenExpressionRef tupleExpr);
BinaryenIndex
BinaryenTupleExtractGetIndex(BinaryenExpressionRef expr);
void BinaryenTupleExtractSetIndex(BinaryenExpressionRef expr,
                                  BinaryenIndex index);
BinaryenExpressionRef
BinaryenI31NewGetValue(BinaryenExpressionRef expr);
void BinaryenI31NewSetValue(BinaryenExpressionRef expr,
                            BinaryenExpressionRef valueExpr);
BinaryenExpressionRef
BinaryenI31GetGetI31(BinaryenExpressionRef expr);
void BinaryenI31GetSetI31(BinaryenExpressionRef expr,
                          BinaryenExpressionRef i31Expr);
bool BinaryenI31GetIsSigned(BinaryenExpressionRef expr);
void BinaryenI31GetSetSigned(BinaryenExpressionRef expr,
                             bool signed_);
BinaryenIndex
BinaryenCallRefGetNumOperands(BinaryenExpressionRef expr);
BinaryenExpressionRef
BinaryenCallRefGetOperandAt(BinaryenExpressionRef expr, BinaryenIndex index);
void BinaryenCallRefSetOperandAt(BinaryenExpressionRef expr,
                                 BinaryenIndex index,
                                 BinaryenExpressionRef operandExpr);
BinaryenIndex BinaryenCallRefAppendOperand(
    BinaryenExpressionRef expr, BinaryenExpressionRef operandExpr);
void BinaryenCallRefInsertOperandAt(BinaryenExpressionRef expr,
                                    BinaryenIndex index,
                                    BinaryenExpressionRef operandExpr);
BinaryenExpressionRef
BinaryenCallRefRemoveOperandAt(BinaryenExpressionRef expr, BinaryenIndex index);
BinaryenExpressionRef
BinaryenCallRefGetTarget(BinaryenExpressionRef expr);
void BinaryenCallRefSetTarget(BinaryenExpressionRef expr,
                              BinaryenExpressionRef targetExpr);
bool BinaryenCallRefIsReturn(BinaryenExpressionRef expr);
void BinaryenCallRefSetReturn(BinaryenExpressionRef expr,
                              bool isReturn);
BinaryenExpressionRef
BinaryenRefTestGetRef(BinaryenExpressionRef expr);
void BinaryenRefTestSetRef(BinaryenExpressionRef expr,
                           BinaryenExpressionRef refExpr);
BinaryenType
BinaryenRefTestGetCastType(BinaryenExpressionRef expr);
void BinaryenRefTestSetCastType(BinaryenExpressionRef expr,
                                BinaryenType intendedType);
BinaryenExpressionRef
BinaryenRefCastGetRef(BinaryenExpressionRef expr);
void BinaryenRefCastSetRef(BinaryenExpressionRef expr,
                           BinaryenExpressionRef refExpr);
BinaryenOp BinaryenBrOnGetOp(BinaryenExpressionRef expr);
void BinaryenBrOnSetOp(BinaryenExpressionRef expr, BinaryenOp op);
const char *BinaryenBrOnGetName(BinaryenExpressionRef expr);
void BinaryenBrOnSetName(BinaryenExpressionRef expr,
                         const char *nameStr);
BinaryenExpressionRef
BinaryenBrOnGetRef(BinaryenExpressionRef expr);
void BinaryenBrOnSetRef(BinaryenExpressionRef expr,
                        BinaryenExpressionRef refExpr);
BinaryenType BinaryenBrOnGetCastType(BinaryenExpressionRef expr);
void BinaryenBrOnSetCastType(BinaryenExpressionRef expr,
                             BinaryenType castType);
BinaryenIndex
BinaryenStructNewGetNumOperands(BinaryenExpressionRef expr);
BinaryenExpressionRef
BinaryenStructNewGetOperandAt(BinaryenExpressionRef expr, BinaryenIndex index);
void BinaryenStructNewSetOperandAt(BinaryenExpressionRef expr,
                                   BinaryenIndex index,
                                   BinaryenExpressionRef operandExpr);
BinaryenIndex BinaryenStructNewAppendOperand(
    BinaryenExpressionRef expr, BinaryenExpressionRef operandExpr);
void BinaryenStructNewInsertOperandAt(BinaryenExpressionRef expr,
                                      BinaryenIndex index,
                                      BinaryenExpressionRef operandExpr);
BinaryenExpressionRef BinaryenStructNewRemoveOperandAt(
    BinaryenExpressionRef expr, BinaryenIndex index);
BinaryenIndex
BinaryenStructGetGetIndex(BinaryenExpressionRef expr);
void BinaryenStructGetSetIndex(BinaryenExpressionRef expr,
                               BinaryenIndex index);
BinaryenExpressionRef
BinaryenStructGetGetRef(BinaryenExpressionRef expr);
void BinaryenStructGetSetRef(BinaryenExpressionRef expr,
                             BinaryenExpressionRef refExpr);
bool BinaryenStructGetIsSigned(BinaryenExpressionRef expr);
void BinaryenStructGetSetSigned(BinaryenExpressionRef expr,
                                bool signed_);
BinaryenIndex
BinaryenStructSetGetIndex(BinaryenExpressionRef expr);
void BinaryenStructSetSetIndex(BinaryenExpressionRef expr,
                               BinaryenIndex index);
BinaryenExpressionRef
BinaryenStructSetGetRef(BinaryenExpressionRef expr);
void BinaryenStructSetSetRef(BinaryenExpressionRef expr,
                             BinaryenExpressionRef refExpr);
BinaryenExpressionRef
BinaryenStructSetGetValue(BinaryenExpressionRef expr);
void BinaryenStructSetSetValue(BinaryenExpressionRef expr,
                               BinaryenExpressionRef valueExpr);
BinaryenExpressionRef
BinaryenArrayNewGetInit(BinaryenExpressionRef expr);
void BinaryenArrayNewSetInit(BinaryenExpressionRef expr,
                             BinaryenExpressionRef initExpr);
BinaryenExpressionRef
BinaryenArrayNewGetSize(BinaryenExpressionRef expr);
void BinaryenArrayNewSetSize(BinaryenExpressionRef expr,
                             BinaryenExpressionRef sizeExpr);
BinaryenIndex
BinaryenArrayNewFixedGetNumValues(BinaryenExpressionRef expr);
BinaryenExpressionRef BinaryenArrayNewFixedGetValueAt(
    BinaryenExpressionRef expr, BinaryenIndex index);
void BinaryenArrayNewFixedSetValueAt(BinaryenExpressionRef expr,
                                     BinaryenIndex index,
                                     BinaryenExpressionRef valueExpr);
BinaryenIndex BinaryenArrayNewFixedAppendValue(
    BinaryenExpressionRef expr, BinaryenExpressionRef valueExpr);
void BinaryenArrayNewFixedInsertValueAt(BinaryenExpressionRef expr,
                                        BinaryenIndex index,
                                        BinaryenExpressionRef valueExpr);
BinaryenExpressionRef BinaryenArrayNewFixedRemoveValueAt(
    BinaryenExpressionRef expr, BinaryenIndex index);
BinaryenExpressionRef
BinaryenArrayGetGetRef(BinaryenExpressionRef expr);
void BinaryenArrayGetSetRef(BinaryenExpressionRef expr,
                            BinaryenExpressionRef refExpr);
BinaryenExpressionRef
BinaryenArrayGetGetIndex(BinaryenExpressionRef expr);
void BinaryenArrayGetSetIndex(BinaryenExpressionRef expr,
                              BinaryenExpressionRef indexExpr);
bool BinaryenArrayGetIsSigned(BinaryenExpressionRef expr);
void BinaryenArrayGetSetSigned(BinaryenExpressionRef expr,
                               bool signed_);
BinaryenExpressionRef
BinaryenArraySetGetRef(BinaryenExpressionRef expr);
void BinaryenArraySetSetRef(BinaryenExpressionRef expr,
                            BinaryenExpressionRef refExpr);
BinaryenExpressionRef
BinaryenArraySetGetIndex(BinaryenExpressionRef expr);
void BinaryenArraySetSetIndex(BinaryenExpressionRef expr,
                              BinaryenExpressionRef indexExpr);
BinaryenExpressionRef
BinaryenArraySetGetValue(BinaryenExpressionRef expr);
void BinaryenArraySetSetValue(BinaryenExpressionRef expr,
                              BinaryenExpressionRef valueExpr);
BinaryenExpressionRef
BinaryenArrayLenGetRef(BinaryenExpressionRef expr);
void BinaryenArrayLenSetRef(BinaryenExpressionRef expr,
                            BinaryenExpressionRef refExpr);
BinaryenExpressionRef
BinaryenArrayCopyGetDestRef(BinaryenExpressionRef expr);
void BinaryenArrayCopySetDestRef(BinaryenExpressionRef expr,
                                 BinaryenExpressionRef destRefExpr);
BinaryenExpressionRef
BinaryenArrayCopyGetDestIndex(BinaryenExpressionRef expr);
void BinaryenArrayCopySetDestIndex(BinaryenExpressionRef expr,
                                   BinaryenExpressionRef destIndexExpr);
BinaryenExpressionRef
BinaryenArrayCopyGetSrcRef(BinaryenExpressionRef expr);
void BinaryenArrayCopySetSrcRef(BinaryenExpressionRef expr,
                                BinaryenExpressionRef srcRefExpr);
BinaryenExpressionRef
BinaryenArrayCopyGetSrcIndex(BinaryenExpressionRef expr);
void BinaryenArrayCopySetSrcIndex(BinaryenExpressionRef expr,
                                  BinaryenExpressionRef srcIndexExpr);
BinaryenExpressionRef
BinaryenArrayCopyGetLength(BinaryenExpressionRef expr);
void BinaryenArrayCopySetLength(BinaryenExpressionRef expr,
                                BinaryenExpressionRef lengthExpr);
BinaryenOp BinaryenStringNewGetOp(BinaryenExpressionRef expr);
void BinaryenStringNewSetOp(BinaryenExpressionRef expr,
                            BinaryenOp op);
BinaryenExpressionRef
BinaryenStringNewGetPtr(BinaryenExpressionRef expr);
void BinaryenStringNewSetPtr(BinaryenExpressionRef expr,
                             BinaryenExpressionRef ptrExpr);
BinaryenExpressionRef
BinaryenStringNewGetLength(BinaryenExpressionRef expr);
void BinaryenStringNewSetLength(BinaryenExpressionRef expr,
                                BinaryenExpressionRef lengthExpr);
BinaryenExpressionRef
BinaryenStringNewGetStart(BinaryenExpressionRef expr);
void BinaryenStringNewSetStart(BinaryenExpressionRef expr,
                               BinaryenExpressionRef startExpr);
BinaryenExpressionRef
BinaryenStringNewGetEnd(BinaryenExpressionRef expr);
void BinaryenStringNewSetEnd(BinaryenExpressionRef expr,
                             BinaryenExpressionRef endExpr);
void BinaryenStringNewSetTry(BinaryenExpressionRef expr,
                             bool try_);
bool BinaryenStringNewIsTry(BinaryenExpressionRef expr);
const char *
BinaryenStringConstGetString(BinaryenExpressionRef expr);
void BinaryenStringConstSetString(BinaryenExpressionRef expr,
                                  const char *stringStr);
BinaryenOp BinaryenStringMeasureGetOp(BinaryenExpressionRef expr);
void BinaryenStringMeasureSetOp(BinaryenExpressionRef expr,
                                BinaryenOp op);
BinaryenExpressionRef
BinaryenStringMeasureGetRef(BinaryenExpressionRef expr);
void BinaryenStringMeasureSetRef(BinaryenExpressionRef expr,
                                 BinaryenExpressionRef refExpr);
BinaryenOp BinaryenStringEncodeGetOp(BinaryenExpressionRef expr);
void BinaryenStringEncodeSetOp(BinaryenExpressionRef expr,
                               BinaryenOp op);
BinaryenExpressionRef
BinaryenStringEncodeGetRef(BinaryenExpressionRef expr);
void BinaryenStringEncodeSetRef(BinaryenExpressionRef expr,
                                BinaryenExpressionRef refExpr);
BinaryenExpressionRef
BinaryenStringEncodeGetPtr(BinaryenExpressionRef expr);
void BinaryenStringEncodeSetPtr(BinaryenExpressionRef expr,
                                BinaryenExpressionRef ptrExpr);
BinaryenExpressionRef
BinaryenStringEncodeGetStart(BinaryenExpressionRef expr);
void BinaryenStringEncodeSetStart(BinaryenExpressionRef expr,
                                  BinaryenExpressionRef startExpr);
BinaryenExpressionRef
BinaryenStringConcatGetLeft(BinaryenExpressionRef expr);
void BinaryenStringConcatSetLeft(BinaryenExpressionRef expr,
                                 BinaryenExpressionRef leftExpr);
BinaryenExpressionRef
BinaryenStringConcatGetRight(BinaryenExpressionRef expr);
void BinaryenStringConcatSetRight(BinaryenExpressionRef expr,
                                  BinaryenExpressionRef rightExpr);
BinaryenOp BinaryenStringEqGetOp(BinaryenExpressionRef expr);
void BinaryenStringEqSetOp(BinaryenExpressionRef expr,
                           BinaryenOp op);
BinaryenExpressionRef
BinaryenStringEqGetLeft(BinaryenExpressionRef expr);
void BinaryenStringEqSetLeft(BinaryenExpressionRef expr,
                             BinaryenExpressionRef leftExpr);
BinaryenExpressionRef
BinaryenStringEqGetRight(BinaryenExpressionRef expr);
void BinaryenStringEqSetRight(BinaryenExpressionRef expr,
                              BinaryenExpressionRef rightExpr);
BinaryenOp BinaryenStringAsGetOp(BinaryenExpressionRef expr);
void BinaryenStringAsSetOp(BinaryenExpressionRef expr,
                           BinaryenOp op);
BinaryenExpressionRef
BinaryenStringAsGetRef(BinaryenExpressionRef expr);
void BinaryenStringAsSetRef(BinaryenExpressionRef expr,
                            BinaryenExpressionRef refExpr);
BinaryenExpressionRef
BinaryenStringWTF8AdvanceGetRef(BinaryenExpressionRef expr);
void BinaryenStringWTF8AdvanceSetRef(BinaryenExpressionRef expr,
                                     BinaryenExpressionRef refExpr);
BinaryenExpressionRef
BinaryenStringWTF8AdvanceGetPos(BinaryenExpressionRef expr);
void BinaryenStringWTF8AdvanceSetPos(BinaryenExpressionRef expr,
                                     BinaryenExpressionRef posExpr);
BinaryenExpressionRef
BinaryenStringWTF8AdvanceGetBytes(BinaryenExpressionRef expr);
void BinaryenStringWTF8AdvanceSetBytes(BinaryenExpressionRef expr,
                                       BinaryenExpressionRef bytesExpr);
BinaryenExpressionRef
BinaryenStringWTF16GetGetRef(BinaryenExpressionRef expr);
void BinaryenStringWTF16GetSetRef(BinaryenExpressionRef expr,
                                  BinaryenExpressionRef refExpr);
BinaryenExpressionRef
BinaryenStringWTF16GetGetPos(BinaryenExpressionRef expr);
void BinaryenStringWTF16GetSetPos(BinaryenExpressionRef expr,
                                  BinaryenExpressionRef posExpr);
BinaryenExpressionRef
BinaryenStringIterNextGetRef(BinaryenExpressionRef expr);
void BinaryenStringIterNextSetRef(BinaryenExpressionRef expr,
                                  BinaryenExpressionRef refExpr);
BinaryenOp BinaryenStringIterMoveGetOp(BinaryenExpressionRef expr);
void BinaryenStringIterMoveSetOp(BinaryenExpressionRef expr,
                                 BinaryenOp op);
BinaryenExpressionRef
BinaryenStringIterMoveGetRef(BinaryenExpressionRef expr);
void BinaryenStringIterMoveSetRef(BinaryenExpressionRef expr,
                                  BinaryenExpressionRef refExpr);
BinaryenExpressionRef
BinaryenStringIterMoveGetNum(BinaryenExpressionRef expr);
void BinaryenStringIterMoveSetNum(BinaryenExpressionRef expr,
                                  BinaryenExpressionRef numExpr);
BinaryenOp BinaryenStringSliceWTFGetOp(BinaryenExpressionRef expr);
void BinaryenStringSliceWTFSetOp(BinaryenExpressionRef expr,
                                 BinaryenOp op);
BinaryenExpressionRef
BinaryenStringSliceWTFGetRef(BinaryenExpressionRef expr);
void BinaryenStringSliceWTFSetRef(BinaryenExpressionRef expr,
                                  BinaryenExpressionRef refExpr);
BinaryenExpressionRef
BinaryenStringSliceWTFGetStart(BinaryenExpressionRef expr);
void BinaryenStringSliceWTFSetStart(BinaryenExpressionRef expr,
                                    BinaryenExpressionRef startExpr);
BinaryenExpressionRef
BinaryenStringSliceWTFGetEnd(BinaryenExpressionRef expr);
void BinaryenStringSliceWTFSetEnd(BinaryenExpressionRef expr,
                                  BinaryenExpressionRef endExpr);
BinaryenExpressionRef
BinaryenStringSliceIterGetRef(BinaryenExpressionRef expr);
void BinaryenStringSliceIterSetRef(BinaryenExpressionRef expr,
                                   BinaryenExpressionRef refExpr);
BinaryenExpressionRef
BinaryenStringSliceIterGetNum(BinaryenExpressionRef expr);
void BinaryenStringSliceIterSetNum(BinaryenExpressionRef expr,
                                   BinaryenExpressionRef numExpr);
typedef struct BinaryenFunction *BinaryenFunctionRef;
;
BinaryenFunctionRef
BinaryenAddFunction(BinaryenModuleRef module,
                    const char *name,
                    BinaryenType params,
                    BinaryenType results,
                    BinaryenType *varTypes,
                    BinaryenIndex numVarTypes,
                    BinaryenExpressionRef body);
BinaryenFunctionRef BinaryenGetFunction(BinaryenModuleRef module,
                                        const char *name);
void BinaryenRemoveFunction(BinaryenModuleRef module,
                            const char *name);
BinaryenIndex BinaryenGetNumFunctions(BinaryenModuleRef module);
BinaryenFunctionRef
BinaryenGetFunctionByIndex(BinaryenModuleRef module, BinaryenIndex index);
void BinaryenAddFunctionImport(BinaryenModuleRef module,
                               const char *internalName,
                               const char *externalModuleName,
                               const char *externalBaseName,
                               BinaryenType params,
                               BinaryenType results);
void BinaryenAddTableImport(BinaryenModuleRef module,
                            const char *internalName,
                            const char *externalModuleName,
                            const char *externalBaseName);
void BinaryenAddMemoryImport(BinaryenModuleRef module,
                             const char *internalName,
                             const char *externalModuleName,
                             const char *externalBaseName,
                             uint8_t shared);
void BinaryenAddGlobalImport(BinaryenModuleRef module,
                             const char *internalName,
                             const char *externalModuleName,
                             const char *externalBaseName,
                             BinaryenType globalType,
                             bool mutable_);
void BinaryenAddTagImport(BinaryenModuleRef module,
                          const char *internalName,
                          const char *externalModuleName,
                          const char *externalBaseName,
                          BinaryenType params,
                          BinaryenType results);
typedef struct BinaryenMemory *BinaryenMemoryRef;
;
typedef struct BinaryenExport *BinaryenExportRef;
;
BinaryenExportRef BinaryenAddFunctionExport(
    BinaryenModuleRef module, const char *internalName, const char *externalName);
BinaryenExportRef BinaryenAddTableExport(BinaryenModuleRef module,
                                         const char *internalName,
                                         const char *externalName);
BinaryenExportRef BinaryenAddMemoryExport(
    BinaryenModuleRef module, const char *internalName, const char *externalName);
BinaryenExportRef BinaryenAddGlobalExport(
    BinaryenModuleRef module, const char *internalName, const char *externalName);
BinaryenExportRef BinaryenAddTagExport(BinaryenModuleRef module,
                                       const char *internalName,
                                       const char *externalName);
BinaryenExportRef BinaryenGetExport(BinaryenModuleRef module,
                                    const char *externalName);
void BinaryenRemoveExport(BinaryenModuleRef module,
                          const char *externalName);
BinaryenIndex BinaryenGetNumExports(BinaryenModuleRef module);
BinaryenExportRef
BinaryenGetExportByIndex(BinaryenModuleRef module, BinaryenIndex index);
typedef struct BinaryenGlobal *BinaryenGlobalRef;
;
BinaryenGlobalRef BinaryenAddGlobal(BinaryenModuleRef module,
                                    const char *name,
                                    BinaryenType type,
                                    bool mutable_,
                                    BinaryenExpressionRef init);
BinaryenGlobalRef BinaryenGetGlobal(BinaryenModuleRef module,
                                    const char *name);
void BinaryenRemoveGlobal(BinaryenModuleRef module,
                          const char *name);
BinaryenIndex BinaryenGetNumGlobals(BinaryenModuleRef module);
BinaryenGlobalRef
BinaryenGetGlobalByIndex(BinaryenModuleRef module, BinaryenIndex index);
typedef struct BinaryenTag *BinaryenTagRef;
;
BinaryenTagRef BinaryenAddTag(BinaryenModuleRef module,
                              const char *name,
                              BinaryenType params,
                              BinaryenType results);
BinaryenTagRef BinaryenGetTag(BinaryenModuleRef module,
                              const char *name);
void BinaryenRemoveTag(BinaryenModuleRef module, const char *name);
typedef struct BinaryenTable *BinaryenTableRef;
;
BinaryenTableRef BinaryenAddTable(BinaryenModuleRef module,
                                  const char *table,
                                  BinaryenIndex initial,
                                  BinaryenIndex maximum,
                                  BinaryenType tableType);
void BinaryenRemoveTable(BinaryenModuleRef module,
                         const char *table);
BinaryenIndex BinaryenGetNumTables(BinaryenModuleRef module);
BinaryenTableRef BinaryenGetTable(BinaryenModuleRef module,
                                  const char *name);
BinaryenTableRef BinaryenGetTableByIndex(BinaryenModuleRef module,
                                         BinaryenIndex index);
typedef struct BinaryenElementSegment *BinaryenElementSegmentRef;
;
BinaryenElementSegmentRef
BinaryenAddActiveElementSegment(BinaryenModuleRef module,
                                const char *table,
                                const char *name,
                                const char **funcNames,
                                BinaryenIndex numFuncNames,
                                BinaryenExpressionRef offset);
BinaryenElementSegmentRef
BinaryenAddPassiveElementSegment(BinaryenModuleRef module,
                                 const char *name,
                                 const char **funcNames,
                                 BinaryenIndex numFuncNames);
void BinaryenRemoveElementSegment(BinaryenModuleRef module,
                                  const char *name);
BinaryenIndex
BinaryenGetNumElementSegments(BinaryenModuleRef module);
BinaryenElementSegmentRef
BinaryenGetElementSegment(BinaryenModuleRef module, const char *name);
BinaryenElementSegmentRef
BinaryenGetElementSegmentByIndex(BinaryenModuleRef module, BinaryenIndex index);
void BinaryenSetMemory(BinaryenModuleRef module,
                       BinaryenIndex initial,
                       BinaryenIndex maximum,
                       const char *exportName,
                       const char **segments,
                       bool *segmentPassive,
                       BinaryenExpressionRef *segmentOffsets,
                       BinaryenIndex *segmentSizes,
                       BinaryenIndex numSegments,
                       bool shared,
                       bool memory64,
                       const char *name);
bool BinaryenHasMemory(BinaryenModuleRef module);
BinaryenIndex BinaryenMemoryGetInitial(BinaryenModuleRef module,
                                       const char *name);
bool BinaryenMemoryHasMax(BinaryenModuleRef module,
                          const char *name);
BinaryenIndex BinaryenMemoryGetMax(BinaryenModuleRef module,
                                   const char *name);
const char *BinaryenMemoryImportGetModule(BinaryenModuleRef module,
                                          const char *name);
const char *BinaryenMemoryImportGetBase(BinaryenModuleRef module,
                                        const char *name);
bool BinaryenMemoryIsShared(BinaryenModuleRef module,
                            const char *name);
bool BinaryenMemoryIs64(BinaryenModuleRef module,
                        const char *name);
uint32_t BinaryenGetNumMemorySegments(BinaryenModuleRef module);
uint32_t
BinaryenGetMemorySegmentByteOffset(BinaryenModuleRef module, BinaryenIndex id);
size_t BinaryenGetMemorySegmentByteLength(BinaryenModuleRef module,
                                          BinaryenIndex id);
bool BinaryenGetMemorySegmentPassive(BinaryenModuleRef module,
                                     BinaryenIndex id);
void BinaryenCopyMemorySegmentData(BinaryenModuleRef module,
                                   BinaryenIndex id,
                                   char *buffer);
void BinaryenSetStart(BinaryenModuleRef module,
                      BinaryenFunctionRef start);
BinaryenFeatures
BinaryenModuleGetFeatures(BinaryenModuleRef module);
void BinaryenModuleSetFeatures(BinaryenModuleRef module,
                               BinaryenFeatures features);
BinaryenModuleRef BinaryenModuleParse(const char *text);
void BinaryenModulePrint(BinaryenModuleRef module);
void BinaryenModulePrintStackIR(BinaryenModuleRef module,
                                bool optimize);
void BinaryenModulePrintAsmjs(BinaryenModuleRef module);
bool BinaryenModuleValidate(BinaryenModuleRef module);
void BinaryenModuleOptimize(BinaryenModuleRef module);
void BinaryenModuleUpdateMaps(BinaryenModuleRef module);
int BinaryenGetOptimizeLevel(void);
void BinaryenSetOptimizeLevel(int level);
int BinaryenGetShrinkLevel(void);
void BinaryenSetShrinkLevel(int level);
bool BinaryenGetDebugInfo(void);
void BinaryenSetDebugInfo(bool on);
bool BinaryenGetLowMemoryUnused(void);
void BinaryenSetLowMemoryUnused(bool on);
bool BinaryenGetZeroFilledMemory(void);
void BinaryenSetZeroFilledMemory(bool on);
bool BinaryenGetFastMath(void);
void BinaryenSetFastMath(bool value);
const char *BinaryenGetPassArgument(const char *name);
void BinaryenSetPassArgument(const char *name, const char *value);
void BinaryenClearPassArguments();
BinaryenIndex BinaryenGetAlwaysInlineMaxSize(void);
void BinaryenSetAlwaysInlineMaxSize(BinaryenIndex size);
BinaryenIndex BinaryenGetFlexibleInlineMaxSize(void);
void BinaryenSetFlexibleInlineMaxSize(BinaryenIndex size);
BinaryenIndex BinaryenGetOneCallerInlineMaxSize(void);
void BinaryenSetOneCallerInlineMaxSize(BinaryenIndex size);
bool BinaryenGetAllowInliningFunctionsWithLoops(void);
void BinaryenSetAllowInliningFunctionsWithLoops(bool enabled);
void BinaryenModuleRunPasses(BinaryenModuleRef module,
                             const char **passes,
                             BinaryenIndex numPasses);
void BinaryenModuleAutoDrop(BinaryenModuleRef module);
size_t BinaryenModuleWrite(BinaryenModuleRef module,
                           char *output,
                           size_t outputSize);
size_t BinaryenModuleWriteText(BinaryenModuleRef module,
                               char *output,
                               size_t outputSize);
size_t BinaryenModuleWriteStackIR(BinaryenModuleRef module,
                                  char *output,
                                  size_t outputSize,
                                  bool optimize);
typedef struct BinaryenBufferSizes
{
  size_t outputBytes;
  size_t sourceMapBytes;
} BinaryenBufferSizes;
BinaryenBufferSizes
BinaryenModuleWriteWithSourceMap(BinaryenModuleRef module,
                                 const char *url,
                                 char *output,
                                 size_t outputSize,
                                 char *sourceMap,
                                 size_t sourceMapSize);
typedef struct BinaryenModuleAllocateAndWriteResult
{
  void *binary;
  size_t binaryBytes;
  char *sourceMap;
} BinaryenModuleAllocateAndWriteResult;
BinaryenModuleAllocateAndWriteResult
BinaryenModuleAllocateAndWrite(BinaryenModuleRef module,
                               const char *sourceMapUrl);
char *BinaryenModuleAllocateAndWriteText(BinaryenModuleRef module);
char *
BinaryenModuleAllocateAndWriteStackIR(BinaryenModuleRef module, bool optimize);
BinaryenModuleRef BinaryenModuleRead(char *input,
                                     size_t inputSize);
void BinaryenModuleInterpret(BinaryenModuleRef module);
BinaryenIndex BinaryenModuleAddDebugInfoFileName(
    BinaryenModuleRef module, const char *filename);
const char *
BinaryenModuleGetDebugInfoFileName(BinaryenModuleRef module,
                                   BinaryenIndex index);
const char *BinaryenFunctionGetName(BinaryenFunctionRef func);
BinaryenType BinaryenFunctionGetParams(BinaryenFunctionRef func);
BinaryenType BinaryenFunctionGetResults(BinaryenFunctionRef func);
BinaryenIndex BinaryenFunctionGetNumVars(BinaryenFunctionRef func);
BinaryenType BinaryenFunctionGetVar(BinaryenFunctionRef func,
                                    BinaryenIndex index);
BinaryenIndex
BinaryenFunctionGetNumLocals(BinaryenFunctionRef func);
bool BinaryenFunctionHasLocalName(BinaryenFunctionRef func,
                                  BinaryenIndex index);
const char *BinaryenFunctionGetLocalName(BinaryenFunctionRef func,
                                         BinaryenIndex index);
void BinaryenFunctionSetLocalName(BinaryenFunctionRef func,
                                  BinaryenIndex index,
                                  const char *name);
BinaryenExpressionRef
BinaryenFunctionGetBody(BinaryenFunctionRef func);
void BinaryenFunctionSetBody(BinaryenFunctionRef func,
                             BinaryenExpressionRef body);
void BinaryenFunctionOptimize(BinaryenFunctionRef func,
                              BinaryenModuleRef module);
void BinaryenFunctionRunPasses(BinaryenFunctionRef func,
                               BinaryenModuleRef module,
                               const char **passes,
                               BinaryenIndex numPasses);
void BinaryenFunctionSetDebugLocation(BinaryenFunctionRef func,
                                      BinaryenExpressionRef expr,
                                      BinaryenIndex fileIndex,
                                      BinaryenIndex lineNumber,
                                      BinaryenIndex columnNumber);
const char *BinaryenTableGetName(BinaryenTableRef table);
void BinaryenTableSetName(BinaryenTableRef table,
                          const char *name);
BinaryenIndex BinaryenTableGetInitial(BinaryenTableRef table);
void BinaryenTableSetInitial(BinaryenTableRef table,
                             BinaryenIndex initial);
bool BinaryenTableHasMax(BinaryenTableRef table);
BinaryenIndex BinaryenTableGetMax(BinaryenTableRef table);
void BinaryenTableSetMax(BinaryenTableRef table,
                         BinaryenIndex max);
const char *
BinaryenElementSegmentGetName(BinaryenElementSegmentRef elem);
void BinaryenElementSegmentSetName(BinaryenElementSegmentRef elem,
                                   const char *name);
const char *
BinaryenElementSegmentGetTable(BinaryenElementSegmentRef elem);
void BinaryenElementSegmentSetTable(BinaryenElementSegmentRef elem,
                                    const char *table);
BinaryenExpressionRef
BinaryenElementSegmentGetOffset(BinaryenElementSegmentRef elem);
BinaryenIndex
BinaryenElementSegmentGetLength(BinaryenElementSegmentRef elem);
const char *
BinaryenElementSegmentGetData(BinaryenElementSegmentRef elem,
                              BinaryenIndex dataId);
bool BinaryenElementSegmentIsPassive(BinaryenElementSegmentRef elem);
const char *BinaryenGlobalGetName(BinaryenGlobalRef global);
BinaryenType BinaryenGlobalGetType(BinaryenGlobalRef global);
bool BinaryenGlobalIsMutable(BinaryenGlobalRef global);
BinaryenExpressionRef
BinaryenGlobalGetInitExpr(BinaryenGlobalRef global);
const char *BinaryenTagGetName(BinaryenTagRef tag);
BinaryenType BinaryenTagGetParams(BinaryenTagRef tag);
BinaryenType BinaryenTagGetResults(BinaryenTagRef tag);
const char *
BinaryenFunctionImportGetModule(BinaryenFunctionRef import);
const char *BinaryenTableImportGetModule(BinaryenTableRef import);
const char *
BinaryenGlobalImportGetModule(BinaryenGlobalRef import);
const char *BinaryenTagImportGetModule(BinaryenTagRef import);
const char *
BinaryenFunctionImportGetBase(BinaryenFunctionRef import);
const char *BinaryenTableImportGetBase(BinaryenTableRef import);
const char *BinaryenGlobalImportGetBase(BinaryenGlobalRef import);
const char *BinaryenTagImportGetBase(BinaryenTagRef import);
BinaryenExternalKind
BinaryenExportGetKind(BinaryenExportRef export_);
const char *BinaryenExportGetName(BinaryenExportRef export_);
const char *BinaryenExportGetValue(BinaryenExportRef export_);
void BinaryenAddCustomSection(BinaryenModuleRef module,
                              const char *name,
                              const char *contents,
                              BinaryenIndex contentsSize);
typedef uint32_t BinaryenSideEffects;
BinaryenSideEffects BinaryenSideEffectNone(void);
BinaryenSideEffects BinaryenSideEffectBranches(void);
BinaryenSideEffects BinaryenSideEffectCalls(void);
BinaryenSideEffects BinaryenSideEffectReadsLocal(void);
BinaryenSideEffects BinaryenSideEffectWritesLocal(void);
BinaryenSideEffects BinaryenSideEffectReadsGlobal(void);
BinaryenSideEffects BinaryenSideEffectWritesGlobal(void);
BinaryenSideEffects BinaryenSideEffectReadsMemory(void);
BinaryenSideEffects BinaryenSideEffectWritesMemory(void);
BinaryenSideEffects BinaryenSideEffectReadsTable(void);
BinaryenSideEffects BinaryenSideEffectWritesTable(void);
BinaryenSideEffects BinaryenSideEffectImplicitTrap(void);
BinaryenSideEffects BinaryenSideEffectTrapsNeverHappen(void);
BinaryenSideEffects BinaryenSideEffectIsAtomic(void);
BinaryenSideEffects BinaryenSideEffectThrows(void);
BinaryenSideEffects BinaryenSideEffectDanglingPop(void);
BinaryenSideEffects BinaryenSideEffectAny(void);
BinaryenSideEffects BinaryenExpressionGetSideEffects(
    BinaryenExpressionRef expr, BinaryenModuleRef module);
typedef struct Relooper *RelooperRef;
typedef struct RelooperBlock *RelooperBlockRef;
RelooperRef RelooperCreate(BinaryenModuleRef module);
RelooperBlockRef RelooperAddBlock(RelooperRef relooper,
                                  BinaryenExpressionRef code);
void RelooperAddBranch(RelooperBlockRef from,
                       RelooperBlockRef to,
                       BinaryenExpressionRef condition,
                       BinaryenExpressionRef code);
RelooperBlockRef
RelooperAddBlockWithSwitch(RelooperRef relooper,
                           BinaryenExpressionRef code,
                           BinaryenExpressionRef condition);
void RelooperAddBranchForSwitch(RelooperBlockRef from,
                                RelooperBlockRef to,
                                BinaryenIndex *indexes,
                                BinaryenIndex numIndexes,
                                BinaryenExpressionRef code);
BinaryenExpressionRef RelooperRenderAndDispose(
    RelooperRef relooper, RelooperBlockRef entry, BinaryenIndex labelHelper);
typedef struct CExpressionRunner *ExpressionRunnerRef;
typedef uint32_t ExpressionRunnerFlags;
ExpressionRunnerFlags ExpressionRunnerFlagsDefault();
ExpressionRunnerFlags ExpressionRunnerFlagsPreserveSideeffects();
ExpressionRunnerFlags ExpressionRunnerFlagsTraverseCalls();
ExpressionRunnerRef
ExpressionRunnerCreate(BinaryenModuleRef module,
                       ExpressionRunnerFlags flags,
                       BinaryenIndex maxDepth,
                       BinaryenIndex maxLoopIterations);
bool ExpressionRunnerSetLocalValue(ExpressionRunnerRef runner,
                                   BinaryenIndex index,
                                   BinaryenExpressionRef value);
bool ExpressionRunnerSetGlobalValue(ExpressionRunnerRef runner,
                                    const char *name,
                                    BinaryenExpressionRef value);
BinaryenExpressionRef ExpressionRunnerRunAndDispose(
    ExpressionRunnerRef runner, BinaryenExpressionRef expr);
typedef struct TypeBuilder *TypeBuilderRef;
typedef uint32_t TypeBuilderErrorReason;
TypeBuilderErrorReason TypeBuilderErrorReasonSelfSupertype(void);
TypeBuilderErrorReason
TypeBuilderErrorReasonInvalidSupertype(void);
TypeBuilderErrorReason
TypeBuilderErrorReasonForwardSupertypeReference(void);
TypeBuilderErrorReason
TypeBuilderErrorReasonForwardChildReference(void);
typedef uint32_t BinaryenBasicHeapType;
TypeBuilderRef TypeBuilderCreate(BinaryenIndex size);
void TypeBuilderGrow(TypeBuilderRef builder, BinaryenIndex count);
BinaryenIndex TypeBuilderGetSize(TypeBuilderRef builder);
void TypeBuilderSetSignatureType(TypeBuilderRef builder,
                                 BinaryenIndex index,
                                 BinaryenType paramTypes,
                                 BinaryenType resultTypes);
void TypeBuilderSetStructType(TypeBuilderRef builder,
                              BinaryenIndex index,
                              BinaryenType *fieldTypes,
                              BinaryenPackedType *fieldPackedTypes,
                              bool *fieldMutables,
                              int numFields);
void TypeBuilderSetArrayType(TypeBuilderRef builder,
                             BinaryenIndex index,
                             BinaryenType elementType,
                             BinaryenPackedType elementPackedType,
                             int elementMutable);
BinaryenHeapType TypeBuilderGetTempHeapType(TypeBuilderRef builder,
                                            BinaryenIndex index);
BinaryenType TypeBuilderGetTempTupleType(TypeBuilderRef builder,
                                         BinaryenType *types,
                                         BinaryenIndex numTypes);
BinaryenType TypeBuilderGetTempRefType(TypeBuilderRef builder,
                                       BinaryenHeapType heapType,
                                       int nullable);
void TypeBuilderSetSubType(TypeBuilderRef builder,
                           BinaryenIndex index,
                           BinaryenHeapType superType);
void TypeBuilderCreateRecGroup(TypeBuilderRef builder,
                               BinaryenIndex index,
                               BinaryenIndex length);
bool TypeBuilderBuildAndDispose(TypeBuilderRef builder,
                                BinaryenHeapType *heapTypes,
                                BinaryenIndex *errorIndex,
                                TypeBuilderErrorReason *errorReason);
void BinaryenModuleSetTypeName(BinaryenModuleRef module,
                               BinaryenHeapType heapType,
                               const char *name);
void BinaryenModuleSetFieldName(BinaryenModuleRef module,
                                BinaryenHeapType heapType,
                                BinaryenIndex index,
                                const char *name);
void BinaryenSetColorsEnabled(bool enabled);
bool BinaryenAreColorsEnabled();
""")

if __name__ == "__main__":
    ffibuilder.compile()