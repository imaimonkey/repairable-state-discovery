# V2R cluster inventory

2026-09-26T04:41:35.630003+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318398603264 available bytes; 82.24% used; 112476278 free inodes.

server1 `/home`: 318398603264 available bytes; 82.24% used; 112476278 free inodes.

server1 `/tmp`: 318398603264 available bytes; 82.24% used; 112476278 free inodes.

server1 `/var/tmp`: 318398603264 available bytes; 82.24% used; 112476278 free inodes.

server1 `/mnt/raid5`: 330488700928 available bytes; 98.48% used; 337545391 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22929285120 available bytes; 98.72% used; 110406198 free inodes.

server2 `/home`: 22929285120 available bytes; 98.72% used; 110406198 free inodes.

server2 `/tmp`: 22929285120 available bytes; 98.72% used; 110406198 free inodes.

server2 `/var/tmp`: 22929285120 available bytes; 98.72% used; 110406198 free inodes.

server2 `/mnt/raid5`: 285165273088 available bytes; 98.03% used; 445050372 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84516257792 available bytes; 95.28% used; 114171889 free inodes.

server3 `/home`: 84516257792 available bytes; 95.28% used; 114171889 free inodes.

server3 `/data`: 124395249664 available bytes; 98.28% used; 225817556 free inodes.

server3 `/tmp`: 84516257792 available bytes; 95.28% used; 114171889 free inodes.

server3 `/var/tmp`: 84516257792 available bytes; 95.28% used; 114171889 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106002100224 available bytes; 94.08% used; 114348206 free inodes.

server4 `/home`: 106002100224 available bytes; 94.08% used; 114348206 free inodes.

server4 `/data`: 107068313600 available bytes; 98.52% used; 224929365 free inodes.

server4 `/tmp`: 106002100224 available bytes; 94.08% used; 114348206 free inodes.

server4 `/var/tmp`: 106002100224 available bytes; 94.08% used; 114348206 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
