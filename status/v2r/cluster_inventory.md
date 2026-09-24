# V2R cluster inventory

2026-09-24T02:50:54.130343+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325385109504 available bytes; 81.85% used; 112498640 free inodes.

server1 `/home`: 325385109504 available bytes; 81.85% used; 112498640 free inodes.

server1 `/tmp`: 325385109504 available bytes; 81.85% used; 112498640 free inodes.

server1 `/var/tmp`: 325385109504 available bytes; 81.85% used; 112498640 free inodes.

server1 `/mnt/raid5`: 558792581120 available bytes; 97.44% used; 337732331 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40874061824 available bytes; 97.72% used; 110431388 free inodes.

server2 `/home`: 40874061824 available bytes; 97.72% used; 110431388 free inodes.

server2 `/tmp`: 40874061824 available bytes; 97.72% used; 110431388 free inodes.

server2 `/var/tmp`: 40874061824 available bytes; 97.72% used; 110431388 free inodes.

server2 `/mnt/raid5`: 528368775168 available bytes; 96.35% used; 445198758 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292344590336 available bytes; 83.69% used; 114196402 free inodes.

server3 `/home`: 292344590336 available bytes; 83.69% used; 114196402 free inodes.

server3 `/data`: 39728406528 available bytes; 99.45% used; 225845919 free inodes.

server3 `/tmp`: 292344590336 available bytes; 83.69% used; 114196402 free inodes.

server3 `/var/tmp`: 292344590336 available bytes; 83.69% used; 114196402 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106002649088 available bytes; 94.08% used; 114349808 free inodes.

server4 `/home`: 106002649088 available bytes; 94.08% used; 114349808 free inodes.

server4 `/data`: 289726095360 available bytes; 96.00% used; 225386982 free inodes.

server4 `/tmp`: 106002649088 available bytes; 94.08% used; 114349808 free inodes.

server4 `/var/tmp`: 106002649088 available bytes; 94.08% used; 114349808 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
