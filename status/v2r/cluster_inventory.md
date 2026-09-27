# V2R cluster inventory

2026-09-27T13:27:40.138258+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304670150656 available bytes; 83.00% used; 112401388 free inodes.

server1 `/home`: 304670150656 available bytes; 83.00% used; 112401388 free inodes.

server1 `/tmp`: 304670150656 available bytes; 83.00% used; 112401388 free inodes.

server1 `/var/tmp`: 304670150656 available bytes; 83.00% used; 112401388 free inodes.

server1 `/mnt/raid5`: 634574155776 available bytes; 97.09% used; 337424228 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 13408280576 available bytes; 99.25% used; 110351829 free inodes.

server2 `/home`: 13408280576 available bytes; 99.25% used; 110351829 free inodes.

server2 `/tmp`: 13408280576 available bytes; 99.25% used; 110351829 free inodes.

server2 `/var/tmp`: 13408280576 available bytes; 99.25% used; 110351829 free inodes.

server2 `/mnt/raid5`: 528809402368 available bytes; 96.35% used; 444733266 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78567391232 available bytes; 95.62% used; 114062841 free inodes.

server3 `/home`: 78567391232 available bytes; 95.62% used; 114062841 free inodes.

server3 `/data`: 1331083165696 available bytes; 81.60% used; 225757442 free inodes.

server3 `/tmp`: 78567391232 available bytes; 95.62% used; 114062841 free inodes.

server3 `/var/tmp`: 78567391232 available bytes; 95.62% used; 114062841 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111010488320 available bytes; 93.81% used; 114372796 free inodes.

server4 `/home`: 111010488320 available bytes; 93.81% used; 114372796 free inodes.

server4 `/data`: 351328059392 available bytes; 95.14% used; 224727741 free inodes.

server4 `/tmp`: 111010488320 available bytes; 93.81% used; 114372796 free inodes.

server4 `/var/tmp`: 111010488320 available bytes; 93.81% used; 114372796 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
