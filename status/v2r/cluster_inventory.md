# V2R cluster inventory

2026-09-26T06:01:01.981996+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318780383232 available bytes; 82.22% used; 112476295 free inodes.

server1 `/home`: 318780383232 available bytes; 82.22% used; 112476295 free inodes.

server1 `/tmp`: 318780383232 available bytes; 82.22% used; 112476295 free inodes.

server1 `/var/tmp`: 318780383232 available bytes; 82.22% used; 112476295 free inodes.

server1 `/mnt/raid5`: 228912996352 available bytes; 98.95% used; 337539970 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22737530880 available bytes; 98.73% used; 110405650 free inodes.

server2 `/home`: 22737530880 available bytes; 98.73% used; 110405650 free inodes.

server2 `/tmp`: 22737530880 available bytes; 98.73% used; 110405650 free inodes.

server2 `/var/tmp`: 22737530880 available bytes; 98.73% used; 110405650 free inodes.

server2 `/mnt/raid5`: 274544033792 available bytes; 98.10% used; 445033657 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82440183808 available bytes; 95.40% used; 114110902 free inodes.

server3 `/home`: 82440183808 available bytes; 95.40% used; 114110902 free inodes.

server3 `/data`: 123991834624 available bytes; 98.29% used; 225822775 free inodes.

server3 `/tmp`: 82440183808 available bytes; 95.40% used; 114110902 free inodes.

server3 `/var/tmp`: 82440183808 available bytes; 95.40% used; 114110902 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106094063616 available bytes; 94.08% used; 114348210 free inodes.

server4 `/home`: 106094063616 available bytes; 94.08% used; 114348210 free inodes.

server4 `/data`: 106984316928 available bytes; 98.52% used; 224929125 free inodes.

server4 `/tmp`: 106094063616 available bytes; 94.08% used; 114348210 free inodes.

server4 `/var/tmp`: 106094063616 available bytes; 94.08% used; 114348210 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
