# V2R cluster inventory

2026-09-24T14:52:09.132916+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324049100800 available bytes; 81.92% used; 112481459 free inodes.

server1 `/home`: 324049100800 available bytes; 81.92% used; 112481459 free inodes.

server1 `/tmp`: 324049100800 available bytes; 81.92% used; 112481459 free inodes.

server1 `/var/tmp`: 324049100800 available bytes; 81.92% used; 112481459 free inodes.

server1 `/mnt/raid5`: 416844795904 available bytes; 98.09% used; 337665639 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57430278144 available bytes; 96.80% used; 110427875 free inodes.

server2 `/home`: 57430278144 available bytes; 96.80% used; 110427875 free inodes.

server2 `/tmp`: 57430278144 available bytes; 96.80% used; 110427875 free inodes.

server2 `/var/tmp`: 57430278144 available bytes; 96.80% used; 110427875 free inodes.

server2 `/mnt/raid5`: 503298912256 available bytes; 96.52% used; 445167086 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84871315456 available bytes; 95.26% used; 114184521 free inodes.

server3 `/home`: 84871315456 available bytes; 95.26% used; 114184521 free inodes.

server3 `/data`: 160662945792 available bytes; 97.78% used; 225807696 free inodes.

server3 `/tmp`: 84871315456 available bytes; 95.26% used; 114184521 free inodes.

server3 `/var/tmp`: 84871315456 available bytes; 95.26% used; 114184521 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105719910400 available bytes; 94.10% used; 114348668 free inodes.

server4 `/home`: 105719910400 available bytes; 94.10% used; 114348668 free inodes.

server4 `/data`: 69164998656 available bytes; 99.04% used; 225256983 free inodes.

server4 `/tmp`: 105719910400 available bytes; 94.10% used; 114348668 free inodes.

server4 `/var/tmp`: 105719910400 available bytes; 94.10% used; 114348668 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
