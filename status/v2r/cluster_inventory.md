# V2R cluster inventory

2026-09-26T05:09:53.399893+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318399102976 available bytes; 82.24% used; 112476282 free inodes.

server1 `/home`: 318399102976 available bytes; 82.24% used; 112476282 free inodes.

server1 `/tmp`: 318399102976 available bytes; 82.24% used; 112476282 free inodes.

server1 `/var/tmp`: 318399102976 available bytes; 82.24% used; 112476282 free inodes.

server1 `/mnt/raid5`: 321130684416 available bytes; 98.53% used; 337543836 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22928056320 available bytes; 98.72% used; 110406192 free inodes.

server2 `/home`: 22928056320 available bytes; 98.72% used; 110406192 free inodes.

server2 `/tmp`: 22928056320 available bytes; 98.72% used; 110406192 free inodes.

server2 `/var/tmp`: 22928056320 available bytes; 98.72% used; 110406192 free inodes.

server2 `/mnt/raid5`: 263626076160 available bytes; 98.18% used; 445049443 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84076548096 available bytes; 95.31% used; 114165378 free inodes.

server3 `/home`: 84076548096 available bytes; 95.31% used; 114165378 free inodes.

server3 `/data`: 124606652416 available bytes; 98.28% used; 225825282 free inodes.

server3 `/tmp`: 84076548096 available bytes; 95.31% used; 114165378 free inodes.

server3 `/var/tmp`: 84076548096 available bytes; 95.31% used; 114165378 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106095534080 available bytes; 94.08% used; 114348206 free inodes.

server4 `/home`: 106095534080 available bytes; 94.08% used; 114348206 free inodes.

server4 `/data`: 106994106368 available bytes; 98.52% used; 224929217 free inodes.

server4 `/tmp`: 106095534080 available bytes; 94.08% used; 114348206 free inodes.

server4 `/var/tmp`: 106095534080 available bytes; 94.08% used; 114348206 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
