# V2R cluster inventory

2026-09-27T01:19:23.834105+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315137007616 available bytes; 82.42% used; 112443434 free inodes.

server1 `/home`: 315137007616 available bytes; 82.42% used; 112443434 free inodes.

server1 `/tmp`: 315137007616 available bytes; 82.42% used; 112443434 free inodes.

server1 `/var/tmp`: 315137007616 available bytes; 82.42% used; 112443434 free inodes.

server1 `/mnt/raid5`: 637547257856 available bytes; 97.08% used; 337405544 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17634246656 available bytes; 99.02% used; 110364996 free inodes.

server2 `/home`: 17634246656 available bytes; 99.02% used; 110364996 free inodes.

server2 `/tmp`: 17634246656 available bytes; 99.02% used; 110364996 free inodes.

server2 `/var/tmp`: 17634246656 available bytes; 99.02% used; 110364996 free inodes.

server2 `/mnt/raid5`: 582469525504 available bytes; 95.98% used; 444886802 free inodes.
| server3 | True | ['0', '3'] | [] | reference_compatible=True |

server3 `/`: 79499247616 available bytes; 95.56% used; 114068702 free inodes.

server3 `/home`: 79499247616 available bytes; 95.56% used; 114068702 free inodes.

server3 `/data`: 1342443102208 available bytes; 81.45% used; 225763741 free inodes.

server3 `/tmp`: 79499247616 available bytes; 95.56% used; 114068702 free inodes.

server3 `/var/tmp`: 79499247616 available bytes; 95.56% used; 114068702 free inodes.
| server4 | True | ['0', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105869709312 available bytes; 94.09% used; 114347843 free inodes.

server4 `/home`: 105869709312 available bytes; 94.09% used; 114347843 free inodes.

server4 `/data`: 406562402304 available bytes; 94.38% used; 224782888 free inodes.

server4 `/tmp`: 105869709312 available bytes; 94.09% used; 114347843 free inodes.

server4 `/var/tmp`: 105869709312 available bytes; 94.09% used; 114347843 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
