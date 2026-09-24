# V2R cluster inventory

2026-09-24T05:20:01.736097+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324569309184 available bytes; 81.89% used; 112492473 free inodes.

server1 `/home`: 324569309184 available bytes; 81.89% used; 112492473 free inodes.

server1 `/tmp`: 324569309184 available bytes; 81.89% used; 112492473 free inodes.

server1 `/var/tmp`: 324569309184 available bytes; 81.89% used; 112492473 free inodes.

server1 `/mnt/raid5`: 506462179328 available bytes; 97.68% used; 337724532 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40747868160 available bytes; 97.73% used; 110430346 free inodes.

server2 `/home`: 40747868160 available bytes; 97.73% used; 110430346 free inodes.

server2 `/tmp`: 40747868160 available bytes; 97.73% used; 110430346 free inodes.

server2 `/var/tmp`: 40747868160 available bytes; 97.73% used; 110430346 free inodes.

server2 `/mnt/raid5`: 522688495616 available bytes; 96.39% used; 445194203 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 291992592384 available bytes; 83.71% used; 114175930 free inodes.

server3 `/home`: 291992592384 available bytes; 83.71% used; 114175930 free inodes.

server3 `/data`: 21153153024 available bytes; 99.71% used; 225839854 free inodes.

server3 `/tmp`: 291992592384 available bytes; 83.71% used; 114175930 free inodes.

server3 `/var/tmp`: 291992592384 available bytes; 83.71% used; 114175930 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105817563136 available bytes; 94.09% used; 114349371 free inodes.

server4 `/home`: 105817563136 available bytes; 94.09% used; 114349371 free inodes.

server4 `/data`: 252566355968 available bytes; 96.51% used; 225366596 free inodes.

server4 `/tmp`: 105817563136 available bytes; 94.09% used; 114349371 free inodes.

server4 `/var/tmp`: 105817563136 available bytes; 94.09% used; 114349371 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
