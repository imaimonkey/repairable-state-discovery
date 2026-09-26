# V2R cluster inventory

2026-09-26T05:53:23.919520+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318780157952 available bytes; 82.22% used; 112476282 free inodes.

server1 `/home`: 318780157952 available bytes; 82.22% used; 112476282 free inodes.

server1 `/tmp`: 318780157952 available bytes; 82.22% used; 112476282 free inodes.

server1 `/var/tmp`: 318780157952 available bytes; 82.22% used; 112476282 free inodes.

server1 `/mnt/raid5`: 234539528192 available bytes; 98.92% used; 337540024 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22737915904 available bytes; 98.73% used; 110405657 free inodes.

server2 `/home`: 22737915904 available bytes; 98.73% used; 110405657 free inodes.

server2 `/tmp`: 22737915904 available bytes; 98.73% used; 110405657 free inodes.

server2 `/var/tmp`: 22737915904 available bytes; 98.73% used; 110405657 free inodes.

server2 `/mnt/raid5`: 275392843776 available bytes; 98.10% used; 445033925 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82785734656 available bytes; 95.38% used; 114132492 free inodes.

server3 `/home`: 82785734656 available bytes; 95.38% used; 114132492 free inodes.

server3 `/data`: 124013576192 available bytes; 98.29% used; 225823332 free inodes.

server3 `/tmp`: 82785734656 available bytes; 95.38% used; 114132492 free inodes.

server3 `/var/tmp`: 82785734656 available bytes; 95.38% used; 114132492 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106094268416 available bytes; 94.08% used; 114348210 free inodes.

server4 `/home`: 106094268416 available bytes; 94.08% used; 114348210 free inodes.

server4 `/data`: 106991329280 available bytes; 98.52% used; 224929126 free inodes.

server4 `/tmp`: 106094268416 available bytes; 94.08% used; 114348210 free inodes.

server4 `/var/tmp`: 106094268416 available bytes; 94.08% used; 114348210 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
