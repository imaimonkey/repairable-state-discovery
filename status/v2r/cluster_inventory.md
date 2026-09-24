# V2R cluster inventory

2026-09-24T04:40:38.520604+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324625580032 available bytes; 81.89% used; 112492894 free inodes.

server1 `/home`: 324625580032 available bytes; 81.89% used; 112492894 free inodes.

server1 `/tmp`: 324625580032 available bytes; 81.89% used; 112492894 free inodes.

server1 `/var/tmp`: 324625580032 available bytes; 81.89% used; 112492894 free inodes.

server1 `/mnt/raid5`: 460149796864 available bytes; 97.89% used; 337724631 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40770732032 available bytes; 97.73% used; 110430482 free inodes.

server2 `/home`: 40770732032 available bytes; 97.73% used; 110430482 free inodes.

server2 `/tmp`: 40770732032 available bytes; 97.73% used; 110430482 free inodes.

server2 `/var/tmp`: 40770732032 available bytes; 97.73% used; 110430482 free inodes.

server2 `/mnt/raid5`: 524747673600 available bytes; 96.37% used; 445195496 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292408238080 available bytes; 83.68% used; 114200454 free inodes.

server3 `/home`: 292408238080 available bytes; 83.68% used; 114200454 free inodes.

server3 `/data`: 24371728384 available bytes; 99.66% used; 225840737 free inodes.

server3 `/tmp`: 292408238080 available bytes; 83.68% used; 114200454 free inodes.

server3 `/var/tmp`: 292408238080 available bytes; 83.68% used; 114200454 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105836470272 available bytes; 94.09% used; 114349407 free inodes.

server4 `/home`: 105836470272 available bytes; 94.09% used; 114349407 free inodes.

server4 `/data`: 253386891264 available bytes; 96.50% used; 225366871 free inodes.

server4 `/tmp`: 105836470272 available bytes; 94.09% used; 114349407 free inodes.

server4 `/var/tmp`: 105836470272 available bytes; 94.09% used; 114349407 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
