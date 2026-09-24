# V2R cluster inventory

2026-09-24T01:00:19.100993+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 325526114304 available bytes; 81.84% used; 112500274 free inodes.

server1 `/home`: 325526114304 available bytes; 81.84% used; 112500274 free inodes.

server1 `/tmp`: 325526114304 available bytes; 81.84% used; 112500274 free inodes.

server1 `/var/tmp`: 325526114304 available bytes; 81.84% used; 112500274 free inodes.

server1 `/mnt/raid5`: 1019002970112 available bytes; 95.33% used; 337734884 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40971165696 available bytes; 97.71% used; 110432213 free inodes.

server2 `/home`: 40971165696 available bytes; 97.71% used; 110432213 free inodes.

server2 `/tmp`: 40971165696 available bytes; 97.71% used; 110432213 free inodes.

server2 `/var/tmp`: 40971165696 available bytes; 97.71% used; 110432213 free inodes.

server2 `/mnt/raid5`: 531834662912 available bytes; 96.33% used; 445202199 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292746051584 available bytes; 83.66% used; 114212041 free inodes.

server3 `/home`: 292746051584 available bytes; 83.66% used; 114212041 free inodes.

server3 `/data`: 82152214528 available bytes; 98.86% used; 225843260 free inodes.

server3 `/tmp`: 292746051584 available bytes; 83.66% used; 114212041 free inodes.

server3 `/var/tmp`: 292746051584 available bytes; 83.66% used; 114212041 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106020216832 available bytes; 94.08% used; 114349541 free inodes.

server4 `/home`: 106020216832 available bytes; 94.08% used; 114349541 free inodes.

server4 `/data`: 292878061568 available bytes; 95.95% used; 225414559 free inodes.

server4 `/tmp`: 106020216832 available bytes; 94.08% used; 114349541 free inodes.

server4 `/var/tmp`: 106020216832 available bytes; 94.08% used; 114349541 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
