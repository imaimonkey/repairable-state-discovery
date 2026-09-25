# V2R cluster inventory

2026-09-25T03:40:39.155401+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318939619328 available bytes; 82.21% used; 112480354 free inodes.

server1 `/home`: 318939619328 available bytes; 82.21% used; 112480354 free inodes.

server1 `/tmp`: 318939619328 available bytes; 82.21% used; 112480354 free inodes.

server1 `/var/tmp`: 318939619328 available bytes; 82.21% used; 112480354 free inodes.

server1 `/mnt/raid5`: 416061509632 available bytes; 98.09% used; 337597685 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22975696896 available bytes; 98.72% used; 110410442 free inodes.

server2 `/home`: 22975696896 available bytes; 98.72% used; 110410442 free inodes.

server2 `/tmp`: 22975696896 available bytes; 98.72% used; 110410442 free inodes.

server2 `/var/tmp`: 22975696896 available bytes; 98.72% used; 110410442 free inodes.

server2 `/mnt/raid5`: 464560398336 available bytes; 96.79% used; 445111370 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84340776960 available bytes; 95.29% used; 114156064 free inodes.

server3 `/home`: 84340776960 available bytes; 95.29% used; 114156064 free inodes.

server3 `/data`: 144421593088 available bytes; 98.00% used; 225817289 free inodes.

server3 `/tmp`: 84340776960 available bytes; 95.29% used; 114156064 free inodes.

server3 `/var/tmp`: 84340776960 available bytes; 95.29% used; 114156064 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105683558400 available bytes; 94.10% used; 114350897 free inodes.

server4 `/home`: 105683558400 available bytes; 94.10% used; 114350897 free inodes.

server4 `/data`: 39158857728 available bytes; 99.46% used; 224965708 free inodes.

server4 `/tmp`: 105683558400 available bytes; 94.10% used; 114350897 free inodes.

server4 `/var/tmp`: 105683558400 available bytes; 94.10% used; 114350897 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
