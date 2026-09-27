# V2R cluster inventory

2026-09-27T01:45:17.759984+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315160940544 available bytes; 82.42% used; 112443377 free inodes.

server1 `/home`: 315160940544 available bytes; 82.42% used; 112443377 free inodes.

server1 `/tmp`: 315160940544 available bytes; 82.42% used; 112443377 free inodes.

server1 `/var/tmp`: 315160940544 available bytes; 82.42% used; 112443377 free inodes.

server1 `/mnt/raid5`: 637506736128 available bytes; 97.08% used; 337405490 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17635684352 available bytes; 99.02% used; 110364996 free inodes.

server2 `/home`: 17635684352 available bytes; 99.02% used; 110364996 free inodes.

server2 `/tmp`: 17635684352 available bytes; 99.02% used; 110364996 free inodes.

server2 `/var/tmp`: 17635684352 available bytes; 99.02% used; 110364996 free inodes.

server2 `/mnt/raid5`: 582244909056 available bytes; 95.98% used; 444885826 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78865117184 available bytes; 95.60% used; 114064255 free inodes.

server3 `/home`: 78865117184 available bytes; 95.60% used; 114064255 free inodes.

server3 `/data`: 1341907722240 available bytes; 81.45% used; 225763029 free inodes.

server3 `/tmp`: 78865117184 available bytes; 95.60% used; 114064255 free inodes.

server3 `/var/tmp`: 78865117184 available bytes; 95.60% used; 114064255 free inodes.
| server4 | True | ['0', '1', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105869078528 available bytes; 94.09% used; 114347846 free inodes.

server4 `/home`: 105869078528 available bytes; 94.09% used; 114347846 free inodes.

server4 `/data`: 406917324800 available bytes; 94.38% used; 224782922 free inodes.

server4 `/tmp`: 105869078528 available bytes; 94.09% used; 114347846 free inodes.

server4 `/var/tmp`: 105869078528 available bytes; 94.09% used; 114347846 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
