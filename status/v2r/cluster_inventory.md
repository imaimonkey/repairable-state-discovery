# V2R cluster inventory

2026-09-25T14:30:51.795065+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319158419456 available bytes; 82.20% used; 112476978 free inodes.

server1 `/home`: 319158419456 available bytes; 82.20% used; 112476978 free inodes.

server1 `/tmp`: 319158419456 available bytes; 82.20% used; 112476978 free inodes.

server1 `/var/tmp`: 319158419456 available bytes; 82.20% used; 112476978 free inodes.

server1 `/mnt/raid5`: 364131569664 available bytes; 98.33% used; 337546829 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 12799700992 available bytes; 99.29% used; 110407876 free inodes.

server2 `/home`: 12799700992 available bytes; 99.29% used; 110407876 free inodes.

server2 `/tmp`: 12799700992 available bytes; 99.29% used; 110407876 free inodes.

server2 `/var/tmp`: 12799700992 available bytes; 99.29% used; 110407876 free inodes.

server2 `/mnt/raid5`: 321476845568 available bytes; 97.78% used; 445075277 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84265775104 available bytes; 95.30% used; 114154470 free inodes.

server3 `/home`: 84265775104 available bytes; 95.30% used; 114154470 free inodes.

server3 `/data`: 142209769472 available bytes; 98.03% used; 225808682 free inodes.

server3 `/tmp`: 84265775104 available bytes; 95.30% used; 114154470 free inodes.

server3 `/var/tmp`: 84265775104 available bytes; 95.30% used; 114154470 free inodes.
| server4 | True | ['2', '3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105654321152 available bytes; 94.10% used; 114349711 free inodes.

server4 `/home`: 105654321152 available bytes; 94.10% used; 114349711 free inodes.

server4 `/data`: 231444598784 available bytes; 96.80% used; 224946355 free inodes.

server4 `/tmp`: 105654321152 available bytes; 94.10% used; 114349711 free inodes.

server4 `/var/tmp`: 105654321152 available bytes; 94.10% used; 114349711 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
