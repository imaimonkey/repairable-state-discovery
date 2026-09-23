# V2R cluster inventory

2026-09-23T15:52:35.682057+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41418723328 available bytes; 97.69% used; 110435193 free inodes.

server2 `/home`: 41418723328 available bytes; 97.69% used; 110435193 free inodes.

server2 `/tmp`: 41418723328 available bytes; 97.69% used; 110435193 free inodes.

server2 `/var/tmp`: 41418723328 available bytes; 97.69% used; 110435193 free inodes.

server2 `/mnt/raid5`: 549195358208 available bytes; 96.21% used; 445223108 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 376855187456 available bytes; 78.97% used; 114285281 free inodes.

server3 `/home`: 376855187456 available bytes; 78.97% used; 114285281 free inodes.

server3 `/data`: 125336436736 available bytes; 98.27% used; 225854752 free inodes.

server3 `/tmp`: 376855187456 available bytes; 78.97% used; 114285281 free inodes.

server3 `/var/tmp`: 376855187456 available bytes; 78.97% used; 114285281 free inodes.
| server4 | True | ['2', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111499251712 available bytes; 93.78% used; 114375780 free inodes.

server4 `/home`: 111499251712 available bytes; 93.78% used; 114375780 free inodes.

server4 `/data`: 37611270144 available bytes; 99.48% used; 225486694 free inodes.

server4 `/tmp`: 111499251712 available bytes; 93.78% used; 114375780 free inodes.

server4 `/var/tmp`: 111499251712 available bytes; 93.78% used; 114375780 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
