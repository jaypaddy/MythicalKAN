          #!/bin/bash

          cat config.json

          APP_NAME=$(jq .APP_NAME config.json)
          CLOUD_BLOB_CONN_STRING=$(jq .CLOUD_BLOB_CONN_STRING config.json)
          EDGE_BLOB_CONN_STRING=$(jq .EDGE_BLOB_CONN_STRING config.json)
          EDGE_BLOB_CONTAINER_NAME=$(jq .EDGE_BLOB_CONTAINER_NAME config.json)
          EDGE_INFERENCE_URL=$(jq .EDGE_INFERENCE_URL config.json)
          LOGGING_LEVEL=$(jq .LOGGING_LEVEL config.json)
          PROMETHEUS_PORT=$(jq .PROMETHEUS_PORT config.json)
          RTSP_URL=$(jq .RTSP_URL config.json)
          SCOPE_KEYS=$(jq .SCOPE_KEYS config.json)
          SCOPE_VALUES=$(jq .SCOPE_VALUES config.json)
          SLEEP_TIME=$(jq .SLEEP_TIME config.json)

          sed -e "s|\"RTSP_URL\"|\"$RTSP_URL\"|g" \
              $(workingDir)/.deployment/manifests/kustomize/overlay/configMap.template.yaml \
                > $(workingDir)/.deployment/manifests/kustomize/overlay/configMap.yaml

          sed -e "s|\"CLOUD_BLOB_CONN_STRING\"|\"$CLOUD_BLOB_CONN_STRING\"|g" \
            $(workingDir)/.deployment/manifests/kustomize/overlay/configMap.yaml \
              > $(workingDir)/.deployment/manifests/kustomize/overlay/configMap.yaml

          sed -e "s|\"EDGE_BLOB_CONN_STRING\"|\"$EDGE_BLOB_CONN_STRING\"|g" \
            $(workingDir)/.deployment/manifests/kustomize/overlay/configMap.yaml \
              > $(workingDir)/.deployment/manifests/kustomize/overlay/configMap.yaml

          sed -e "s|\"EDGE_INFERENCE_URL\"|\"$EDGE_INFERENCE_URL\"|g" \
            $(workingDir)/.deployment/manifests/kustomize/overlay/configMap.yaml \
              > $(workingDir)/.deployment/manifests/kustomize/overlay/configMap.yaml

          sed -e "s|\"EDGE_BLOB_CONTAINER_NAME\"|\"$EDGE_BLOB_CONTAINER_NAME\"|g" \
            $(workingDir)/.deployment/manifests/kustomize/overlay/configMap.yaml \
              > $(workingDir)/.deployment/manifests/kustomize/overlay/configMap.yaml

          sed -e "s|\"LOGGING_LEVEL\"|\"$LOGGING_LEVEL\"|g" \
            $(workingDir)/.deployment/manifests/kustomize/overlay/configMap.yaml \
              > $(workingDir)/.deployment/manifests/kustomize/overlay/configMap.yaml

          sed -e "s|\"APP_NAME\"|\"$APP_NAME\"|g" \
            $(workingDir)/.deployment/manifests/kustomize/overlay/configMap.yaml \
              > $(workingDir)/.deployment/manifests/kustomize/overlay/configMap.yaml

          sed -e "s|\"SCOPE_KEYS\"|\"$SCOPE_KEYS\")"|g" \
            $(workingDir)/.deployment/manifests/kustomize/overlay/configMap.yaml \
              > $(workingDir)/.deployment/manifests/kustomize/overlay/configMap.yaml

          sed -e "s|\"SCOPE_VALUES\"|\"$SCOPE_VALUES\"|g" \
            $(workingDir)/.deployment/manifests/kustomize/overlay/configMap.yaml \
              > $(workingDir)/.deployment/manifests/kustomize/overlay/configMap.yaml
              
          sed -e "s|\"PROMETHEUS_PORT\"|\"$PROMETHEUS_PORT\"|g" \
            $(workingDir)/.deployment/manifests/kustomize/overlay/configMap.yaml \
              > $(workingDir)/.deployment/manifests/kustomize/overlay/configMap.yaml
