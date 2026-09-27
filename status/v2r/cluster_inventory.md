# V2R cluster inventory

2026-09-27T10:50:40.307686+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314432147456 available bytes; 82.46% used; 112440713 free inodes.

server1 `/home`: 314432147456 available bytes; 82.46% used; 112440713 free inodes.

server1 `/tmp`: 314432147456 available bytes; 82.46% used; 112440713 free inodes.

server1 `/var/tmp`: 314432147456 available bytes; 82.46% used; 112440713 free inodes.

server1 `/mnt/raid5`: 635409870848 available bytes; 97.09% used; 337424412 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16499519488 available bytes; 99.08% used; 110355937 free inodes.

server2 `/home`: 16499519488 available bytes; 99.08% used; 110355937 free inodes.

server2 `/tmp`: 16499519488 available bytes; 99.08% used; 110355937 free inodes.

server2 `/var/tmp`: 16499519488 available bytes; 99.08% used; 110355937 free inodes.

server2 `/mnt/raid5`: 571203547136 available bytes; 96.05% used; 444738061 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78544601088 available bytes; 95.62% used; 114062823 free inodes.

server3 `/home`: 78544601088 available bytes; 95.62% used; 114062823 free inodes.

server3 `/data`: 1332053786624 available bytes; 81.59% used; 225760640 free inodes.

server3 `/tmp`: 78544601088 available bytes; 95.62% used; 114062823 free inodes.

server3 `/var/tmp`: 78544601088 available bytes; 95.62% used; 114062823 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111031349248 available bytes; 93.80% used; 114372822 free inodes.

server4 `/home`: 111031349248 available bytes; 93.80% used; 114372822 free inodes.

server4 `/data`: 363141607424 available bytes; 94.98% used; 224766847 free inodes.

server4 `/tmp`: 111031349248 available bytes; 93.80% used; 114372822 free inodes.

server4 `/var/tmp`: 111031349248 available bytes; 93.80% used; 114372822 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
