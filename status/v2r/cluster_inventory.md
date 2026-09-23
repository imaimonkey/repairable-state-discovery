# V2R cluster inventory

2026-09-23T19:05:01.138184+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325897277440 available bytes; 81.82% used; 112504020 free inodes.

server1 `/home`: 325897277440 available bytes; 81.82% used; 112504020 free inodes.

server1 `/tmp`: 325897277440 available bytes; 81.82% used; 112504020 free inodes.

server1 `/var/tmp`: 325897277440 available bytes; 81.82% used; 112504020 free inodes.

server1 `/mnt/raid5`: 1389246803968 available bytes; 93.63% used; 337741432 free inodes.
| server2 | True | ['6', '7'] | [] | reference_compatible=False |

server2 `/`: 41338757120 available bytes; 97.69% used; 110435436 free inodes.

server2 `/home`: 41338757120 available bytes; 97.69% used; 110435436 free inodes.

server2 `/tmp`: 41338757120 available bytes; 97.69% used; 110435436 free inodes.

server2 `/var/tmp`: 41338757120 available bytes; 97.69% used; 110435436 free inodes.

server2 `/mnt/raid5`: 543898898432 available bytes; 96.24% used; 445213447 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 293343035392 available bytes; 83.63% used; 114219638 free inodes.

server3 `/home`: 293343035392 available bytes; 83.63% used; 114219638 free inodes.

server3 `/data`: 52776964096 available bytes; 99.27% used; 225845973 free inodes.

server3 `/tmp`: 293343035392 available bytes; 83.63% used; 114219638 free inodes.

server3 `/var/tmp`: 293343035392 available bytes; 83.63% used; 114219638 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106475433984 available bytes; 94.06% used; 114356232 free inodes.

server4 `/home`: 106475433984 available bytes; 94.06% used; 114356232 free inodes.

server4 `/data`: 15437824 available bytes; 100.00% used; 225457663 free inodes.

server4 `/tmp`: 106475433984 available bytes; 94.06% used; 114356232 free inodes.

server4 `/var/tmp`: 106475433984 available bytes; 94.06% used; 114356232 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
