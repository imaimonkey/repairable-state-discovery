# V2R cluster inventory

2026-09-27T03:51:44.531858+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315076321280 available bytes; 82.42% used; 112443040 free inodes.

server1 `/home`: 315076321280 available bytes; 82.42% used; 112443040 free inodes.

server1 `/tmp`: 315076321280 available bytes; 82.42% used; 112443040 free inodes.

server1 `/var/tmp`: 315076321280 available bytes; 82.42% used; 112443040 free inodes.

server1 `/mnt/raid5`: 636787228672 available bytes; 97.08% used; 337401379 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17623375872 available bytes; 99.02% used; 110365007 free inodes.

server2 `/home`: 17623375872 available bytes; 99.02% used; 110365007 free inodes.

server2 `/tmp`: 17623375872 available bytes; 99.02% used; 110365007 free inodes.

server2 `/var/tmp`: 17623375872 available bytes; 99.02% used; 110365007 free inodes.

server2 `/mnt/raid5`: 578046656512 available bytes; 96.01% used; 444882035 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78697709568 available bytes; 95.61% used; 114062936 free inodes.

server3 `/home`: 78697709568 available bytes; 95.61% used; 114062936 free inodes.

server3 `/data`: 1335357214720 available bytes; 81.54% used; 225761236 free inodes.

server3 `/tmp`: 78697709568 available bytes; 95.61% used; 114062936 free inodes.

server3 `/var/tmp`: 78697709568 available bytes; 95.61% used; 114062936 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111027548160 available bytes; 93.80% used; 114372963 free inodes.

server4 `/home`: 111027548160 available bytes; 93.80% used; 114372963 free inodes.

server4 `/data`: 383849902080 available bytes; 94.70% used; 224780820 free inodes.

server4 `/tmp`: 111027548160 available bytes; 93.80% used; 114372963 free inodes.

server4 `/var/tmp`: 111027548160 available bytes; 93.80% used; 114372963 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
